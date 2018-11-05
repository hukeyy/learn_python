#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, pickle
from conf.settings import main_db_file
from model.school import School
from model.tools import file_oper, option

class School_center(object):
    school_list = ['创建课程', '创建班级', '招聘讲师', '返回']

    def __init__(self):
        if not os.path.exists(main_db_file):
            self.init_database()
        self.run()
    
    def init_database(self):
        sh = School('上海', '上海市')
        bj = School('北京', '北京市')
        data = {'上海':sh, '北京':bj}
        file_oper(main_db_file, 'wb', data)

    def run(self):
        Flag = True
        while Flag:
            self.school_db = file_oper(main_db_file, 'rb')
            if self.school_db:
                for key in self.school_db:
                    print('学校名【%s】' % key)
                school_name = input('\033[34;1m选择学校名:\033[0m').strip()
                if school_name in self.school_db:
                    self.school_name = school_name
                    self.school = self.school_db[school_name]
            while Flag:
                choice = option(School_center.school_list)
                if choice == '1':
                    self.add_course()
                elif choice == '2':
                    self.add_grade()
                elif choice == '3':
                    self.hire_teacher()
                elif choice == '4':
                    Flag = False

    def add_course(self):
        while True:
            if self.school.school_course:
                for key in self.school.school_course:
                    course_obj = self.school.school_course[key]
                    course_obj.cat_course()
            if_cont = input('是否创建课程[y/b]:').strip()
            if if_cont == 'y':
                course_name = input('\033[34;1m输入课程名:\033[0m').strip()
                if course_name not in self.school.school_course:
                    course_price = input('\033[34;1m输入课程价格:\033[0m').strip()
                    course_time = input('\033[34;1m输入课程周期:\033[0m').strip()
                    self.school.create_course(course_name, course_price, course_time)
                    self.school_db[self.school_name] = self.school
                    file_oper(main_db_file, 'wb', self.school_db)
                else:
                    print('\033[31;1m课程【%s】已存在.\033[0m' % course_name)
            elif if_cont == 'b':
                break


    def add_grade(self):
        pass
    def hire_teacher(self):
        pass
            



