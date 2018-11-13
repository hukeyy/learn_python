#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
from core.manage_school import School_center
from core.manage_student import Student_center
from core.teacher_center import Teacher_center


class Manage_center(object):
    def __init__(self):
        pass
    def run(self):
        while True:
            print('1. 学校中心\n'
                  '2. 讲师中心\n'
                  '3. 学生中心\n'
                  '4. 退出')
            user_choice = input('>>>').strip()
            if user_choice == '1':
                School_center()
            elif user_choice == '2':
                Teacher_center()
            elif user_choice == '3':
                Student_center()
            elif user_choice == '4':
                break
            else:
                print('\033[31;1m输入错误，请重新输入.\033[0m')
                
