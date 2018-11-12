#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, shelve
from conf.settings import school_db_file

class Student_center(object):
    def __init__(self):
        if os.path.exists(school_db_file + '.dat'):
            self.school_db = shelve.open(school_db_file)
            self.mange_run()
            self.school_db.close()
        else:
            print('\033[31;1m数据库文件不存在，请先初始化数据库.\033[0m')

    def mange_run(self):
        print('\033[32;1m欢迎进入学生中心\033[0m')
        for key in self.school_db:
            print('学校名：', key)
        choice_school = input('\033[34;1m输入学校名:\033[0m').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            student_name = input('\033[34;1m输入学生名:\033[0m').strip()
            student_age = input('\033[34;1m输入学生年龄:\033[0m').strip()
            self.school_obj.show_grade_course()
            student_grade = input('\033[34;1m请选择班级名:\033[0m').strip()
            if student_grade in self.school_obj.school_grade:
                self.school_obj.create_student(student_name, student_age, student_grade)
                self.school_db.update({self.choice_school: self.school_obj})
                print('\033[32;1m学生注册成功.\033[0m')
            else:
                print('\033[31;1m班级信息不存在.\033[0m')
        else:
            print('\033[31;1m输入的学校不存在.\033[0m')



























