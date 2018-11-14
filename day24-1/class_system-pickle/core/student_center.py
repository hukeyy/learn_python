#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys, pickle
from conf.settings import school_db_file
from modules.tools import file_oper
from modules.school import School


class Student_center(object):
    def __init__(self):
        if os.path.exists(school_db_file):
            self.school_db = file_oper(school_db_file, 'rb')
            self.manage_run()
        else:
            print('\033[31;1m数据库文件不存在，请先初始化.\033[0m')

    def manage_run(self):
        for key in self.school_db:
            print('学校名：', key)
        choice_school = input('>>>').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            student_name = input('\033[34;1m输入学生名:\033[0m').strip()
            student_age = input('\033[34;1m输入学生年龄:\033[0m').strip()
            self.school_obj.show_grade_course()
            grade_name = input('\033[34;1m输入要选择的班级名:\033[0m')
            if grade_name in self.school_obj.school_grade:
                self.school_obj.create_student(student_name, student_age, grade_name)
                self.school_db[self.choice_school] = self.school_obj
                file_oper(school_db_file, 'wb', self.school_db)
                print('\033[32;1m选课成功.\033[0m')

            else:
                print('\033[31;1m班级信息不存在.\033[0m')
