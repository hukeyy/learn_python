#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, shelve
from conf.settings import main_file_db

class Manage_student(object):
    def __init__(self):
        if os.path.exists(main_file_db + '.dat'):
            self.school_db = shelve.open(main_file_db)
            self.manage_run()
            self.school_db.close()
        else:
            print('\033[31;1m数据库文件不存在，请先创建数据库文件.\033[0m')

    def manage_run(self):
        for key in self.school_db:
            print('学校名:', key)
        choice_school = input('\033[34;1m选择学校名:\033[0m').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[self.choice_school]
            student_name = input('\033[34;1m选择学生名:\033[0m').strip()
            student_age = input('\033[34;1m选择学生年龄:\033[0m').strip()
            self.school_obj.show_grade_course()
            choice_grade = input('\033[34;1m选择班级名:\033[0m').strip()
            if choice_grade in self.school_obj.school_grade:
                self.school_obj.create_student(student_name, student_age, choice_grade)
                self.school_db.update({self.choice_school: self.school_obj})
                print('\033[32;1m学员注册成功.\033[0m')
            else:
                print('\033[31;1m班级信息不存在.\033[0m')
        else:
            print('\033[31;1m学校信息不存在.\033[0m')













