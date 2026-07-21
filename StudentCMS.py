"""
管理系统的界面
"""

from Student import Student

class StudentCMS:
    def __init__(self):
        stu_list = []


    # 添加学员信息
    def add_student(self):
        pass

    # 删除学员信息
    def delete_student(self):
        pass

    # 修改学员信息
    def update_student(self):
        pass

    # 查询单个学员信息
    def search_one_student(self):
        pass

    # 查询所有学员信息
    def search_all_students(self):
        pass

    # 保存学员信息
    def save_student(self):
        pass

    # 加载学员信息
    def load_student(self):
        pass

    # 操作界面
    def show_student(self):
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


        while True:
            self.show_student()
            input_num = input("请选择您的操作：")
            if input_num == "1":
                print("添加学员信息\n")
                self.add_student()

            elif input_num == "2":
                print("修改学员信息:\n")
                self.update_student()

            elif input_num == "3":
                print("删除学员信息\n")
                self.delete_student()

            elif input_num == "4":
                print("查询某个学员\n")
                self.search_one_student()

            elif input_num == "5":
                print("显示所有学员\n")
                self.search_all_students()

            elif input_num == "6":
                print("保存信息\n")
                self.save_student()

            elif input_num == "0":
                flag_num = input("请二次确定操作(Y/N) -> ")
                if flag_num.lower() == "y":
                    print("退出系统成功！祝您愉快\n")
                    break
                else:
                    print("退出操作取消!\n")


            else:
                print("非法操作，请重新选择！\n")







if __name__ == '__main__':
    s1 = StudentCMS()
    s1.start()