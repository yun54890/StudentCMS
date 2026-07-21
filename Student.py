"""
此文件用来初始化学生属性,属性有姓名、年龄、性别、联系方式、描述信息
"""

class Student:
    def __init__(self, name, age,gender,phone,desc):
        """
        该魔法方法是初始化学生类属性
        :param name: 名字
        :param age: 年龄
        :param gender: 性别
        :param phone: 手机号
        :param desc: 描述信息
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.desc = desc

    def __str__(self):
        """
        输出对象信息
        :return: 姓名，年龄，性别，手机号，描述信息
        """
        return f'姓名：{self.name} 年龄：{self.age} 性别：{self.gender} 手机号：{self.phone} 描述信息：{self.desc}'


if __name__ == '__main__':
    s1 = Student("张三",19,"男",'18012341234',"大学本科计算机一班")
    print(s1)