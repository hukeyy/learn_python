#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
from core.school_center import School_center
from core.student_center import Student_center


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
                pass
            elif user_choice == '3':
                Student_center()
            elif user_choice == '4':
                break
                
                
        