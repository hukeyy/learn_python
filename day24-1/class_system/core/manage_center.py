#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
from core.manage_school import Manage_school
from core.student_center import Manage_student
from core.teacher_center import Manage_teacher

class Manage_center(object):
    def __init__(self):
        pass
    def run(self):
        while True:
            print('\n欢迎使用选课系统\n'
                  '1. 学校中心\n'
                  '2. 讲师中心\n'
                  '3. 学生中心\n'
                  '4. 退出')
            user_choice = input('>>>').strip()
            if user_choice == '1':
                Manage_school()
            elif user_choice == '2':
                Manage_teacher()
                pass
            elif user_choice == '3':
                Manage_student()
            elif user_choice == '4':
                break
            else:
                print('\033[31;1m输入错误，请重新输入.\033[0m')

