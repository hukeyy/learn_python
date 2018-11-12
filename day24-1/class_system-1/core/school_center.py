#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, shelve, sys
from conf.settings import main_db_file
from modules.school import School

class School_center(object):
    def __init__(self):
        if not os.path.exists(main_db_file):
            self.init_school()
            self.manage_run()
            self.school_db.close()
        else:
            self.school_db = shelve.open(main_db_file)
            self.manage_run()
            self.school_db.close()
    
    def init_school(self):
        self.school_db = shelve.open(main_db_file)
        self.school_db['北京'] = School('北京', '北京市')
        self.school_db['上海'] = School('上海', '上海市')

    def manage_run(self):
        for key in self.school_db:
            print('学校名：', key)
        choice_school = input('\033[34;1m输入学校名:\033[0m').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            while True:
                print('\n欢迎进入【%s】校区\n'
                      '创建课程 add_course\n'
                      '查看课程 check_course\n'
                      '创建班级 add_grade\n'
                      '查看班级 check_grade\n'
                      '创建讲师 add_teacher\n'
                      '查看讲师 check_teacher\n'
                      '退出系统 exit' % choice_school)
                
                user_func = input('>>>').strip()
                if hasattr(self, user_func):
                    getattr(self, user_func)()
    
    def add_course(self):
        course_name = input('\033[34;1m输入课程名:\033[0m')
        course_price = input('\033[34;1m输入课程价格:\033[0m')
        course_time = input('\033[34;1m输入课程周期:\033[0m')
        if course_name in self.school_obj.school_course:
            print('\033[31;1m课程已存在.\033[0m')
            self.school_obj.create_course(course_name, course_price, course_time)
            print('\033[32;1m课程更新成功.\033[0m')
        else:
            self.school_obj.create_course(course_name, course_price, course_time)
            print('\033[32;1m课程新增成功.\033[0m')

    def check_course(self):
        self.school_obj.show_course()






        
    def exit(self, *args):
        self.school_db.close()
        sys.exit('欢迎下次使用选课系统.')
                
            



































