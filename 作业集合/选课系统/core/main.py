# -*- coding: utf-8 -*-
# Author: hkey
class Manage_center(object):
    def __init__(self):
        pass

    def run(self):
        while True:
            print('\n欢迎进入选课系统\n'
                  '1. 学生视图\n'
                  '2. 教师视图\n'
                  '3. 学校视图\n'
                  'q 退出学员管理系统\n')
            user_choice = input('\033[34;0m请输入您要登录的视图：\033[0m')
            if user_choice == '1':
                Manage_student()
            elif user_choice == '2':
                Manage_teacher()
            elif user_choice == '3':
                Manage_school()
            elif user_choice == 'q':
                print('\033[42;1m感谢使用学员管理系统，退出\033[0m')
                break
            else:
                print('\033[31;1m请输入正确的选项\033[0m')

class Manage_student(object):
    pass

class Manage_teacher(object):
    pass

class Manage_school(object):
    pass