"""
管理系统的界面
"""

from Student import Student
import json

class StudentCMS:
    def __init__(self):
        self.stu_list = []
        # 测试数据列表
        # self.stu_list = [
        #     Student("张三", 20, "男", "12312341234", "大学本科计算机专业"),
        #     Student("李四", 19, "女", "13800138000", "软件技术大一新生"),
        #     Student("王五", 21, "男", "13900139000", "嵌入式方向爱好者"),
        #     Student("赵六", 20, "女", "13700137000", "Python后端学习者"),
        #     Student("陈七", 22, "男", "13600136000", "准备软考软件设计师")
        # ]

    # 添加学员信息
    def add_student(self):
        stu_name = input("请输入学生姓名：")
        stu_age = input("请输入学生年龄：")
        stu_gender = input("请输入学生性别：")
        stu_phone = input("请输入学生手机号：")
        stu_desc = input("请输入学生描述信息：")
        list = Student(stu_name, stu_age, stu_gender, stu_phone,stu_desc)
        self.stu_list.append(list)
        print("添加学生信息成功！\n")

    # 删除学员信息
    def delete_student(self):
        del_name = input("请输入您要删除的学员姓名：")
        for stu in self.stu_list:
            if stu.name == del_name:
                self.stu_list.remove(stu)
                print("删除学员信息成功！\n")
                break
        else:
            print("暂无有这个学员信息...\n")

    # 修改学员信息
    def update_student(self):
        update_name = input("请输入您要修改的学员信息姓名：")
        for stu in self.stu_list:
            if stu.name == update_name:
                stu.age = input("请输入您要修改的年龄：")
                stu.gender = input("请输入您要修改的性别：")
                stu.phone = input("请输入您要修改的手机号：")
                stu.desc = input("请输入您要修改的描述：")
                print("修改学员信息成功！\n")
                break
        else:
            print("暂无有这个学员信息...\n")

    # 查询单个学员信息
    def search_one_student(self):
        search_name = input("请选择您要查询的学员姓名：")
        for stu in self.stu_list:
            if stu.name == search_name:
                print(stu)
                print()
                break
        else:
            print("暂无有这个学员信息...\n")

    # 查询所有学员信息
    def search_all_students(self):
        if len(self.stu_list) == 0:
            print("暂无学员信息...\n")
        else:
            for stu in self.stu_list:
                print(stu)

    # 保存学员信息
    def save_student(self):
        # 对象 -> 字典
        data = [stu.__dict__ for stu in self.stu_list]
        with open("students.json","w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=4)

    # 加载学员信息
    def load_student(self):
        # 字典 -> 对象
        try:
            with open("students.json","r",encoding="utf-8") as f:
                data = json.load(f)
            self.stu_list = [Student(**data_dict) for data_dict in data]
        except:
            with open("students.json","w",encoding="utf-8") as f:
                pass

    # 操作界面
    @staticmethod
    def show_student():
        """
        显示操作页面
        :return:
        """
        print("*"*35)
        print("本学员管理系统v2.0可完成如下操作")
        print("\t1.添加学员;")
        print("\t2.修改学员;")
        print("\t3.删除学员;")
        print("\t4.查询某个学员;")
        print("\t5.显示所有学员;")
        print("\t6.保存信息;")
        print("\t0.退出系统.")
        print("*"*35)

    def start(self):

        self.load_student()
        while True:
            StudentCMS.show_student()
            input_num = input("请选择您的操作：")
            if input_num == "1":
                # print("添加学员信息\n")
                self.add_student()

            elif input_num == "2":
                # print("修改学员信息:\n")
                self.update_student()

            elif input_num == "3":
                # print("删除学员信息\n")
                self.delete_student()

            elif input_num == "4":
                # print("查询某个学员\n")
                self.search_one_student()

            elif input_num == "5":
                # print("显示所有学员\n")
                self.search_all_students()

            elif input_num == "6":
                # print("保存信息\n")
                self.save_student()

            elif input_num == "0":
                flag_num = input("请二次确定操作(Y/N) -> ")
                if flag_num.lower() == "y":
                    self.save_student()
                    print("退出系统成功！祝您愉快\n")
                    break
                else:
                    print("退出操作取消!\n")


            else:
                print("非法操作，请重新选择！\n")