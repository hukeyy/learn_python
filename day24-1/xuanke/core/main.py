#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, shelve
from conf.settings import school_db_file
from modules.school import School


class Manage_center(object):
    def __init__(self):
        pass
    def run(self):
        while True:
            print('\n欢迎使用CLASS_SYSTEM系统\n'
                  '1. 学校中心\n'
                  '2. 讲师中心\n'
                  '3. 学生中心\n'
                  '4. 退出')
            choice = input('>>>').strip()
            if choice == '1':
                Manage_school()
            elif choice == '2':
                # Manage_teacher()
                pass
            elif choice == '3':
                # Manage_student()
                pass
            elif choice == '4':
                break
            else:
                print('\033[31;1m输入错误，请重新输入.\033[0m')


class Manage_school(object):
    def __init__(self):
        if not os.path.exists(school_db_file + '.dat'):
            self.init_school()
            self.manage_run()
            self.school_db.close()
        else:
            self.school_db = shelve.open(school_db_file)
            self.manage_run()
            self.school_db.close()

    def init_school(self):
        self.school_db = shelve.open(school_db_file)
        self.school_db['上海'] = School('上海', '上海市')
        self.school_db['北京'] = School('北京', '北京市')

    def manage_run(self):
        for key in self.school_db:
            print('学校名:', key)
        
        choice_school = input('>>>').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            while True:
                print('\n欢迎进入【%s】学区\n'
                      '创建课程 add_course\n'
                      '查看课程 check_course\n'
                      '退出系统 exit')
                user_choice = input('>>>').strip()
                if hasattr(self, user_choice):
                    getattr(self, user_choice)()
    
    def add_course(self):
        course_name = input('\033[34;1m输入课程名:\033[0m').strip()
        course_price = input('\033[34;1m输入课程价格:\033[0m').strip()
        course_time = input('\033[34;1m输入课程周期:\033[0m').strip()

            
                
                

