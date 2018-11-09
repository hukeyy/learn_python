#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, shelve
from conf.settings import main_file_db


class Student_center(object):
    def __init__(self):
        if os.path.exists(main_file_db + '.dat'):
            self.school_db = shelve.open(main_file_db)
            self.run_manage()
            self.school_db.close()
        else:
            print('\033[31;1m数据文件不存在，请先创建学校.\033[0m')
            exit()

    def run_manage(self):
        for key in self.school_db:
            print('学校名:', key)
        choice_school = input('\033[34;1m输入要注册的学校名:').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            student_name = input('\033[34;1m输入学生名:\033[0m').strip()
            student_age = input('\033[34;1m输入学生年龄:\033[0m').strip()
            self.school_obj.show_grade_course()
            grade_name = input('\033[34;1m选择要上课的班级名:\033[0m').strip()
            if grade_name in self.school_obj.school_grade:
                self.school_obj.create_student(student_name, student_age, grade_name)
                self.school_db.update({self.choice_school: self.school_obj})
                print('\033[31;1m学生注册成功.\033[0m')
            else:
                print('\033[31;1m输入的班级不存在, 请先创建班级信息.\033[0m')
        else:
            print('\033[31;1m输入的学校名不存在，请重新输入.\033[0m')




























