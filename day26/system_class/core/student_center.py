#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, shelve
from conf.settings import school_file_db


class Student_center(object):
    def __init__(self):
        if os.path.exists(school_file_db + '.dat'):
            self.school_db = shelve.open(school_file_db)
            self.manage_run()
            self.school_db.close()
        else:
            print('\033[31;1m请先初始化数据库信息.\033[0m')
            exit(1)

    def manage_run(self):
        for key in self.school_db:
            print('学校名：', key)
        choice_school = input('>>>').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            print('\n欢迎进入学员中心\n')
            student_name = input('\033[34;1m输入学员名:\033[0m').strip()
            student_age = input('\033[34;1m输入学员年龄:\033[0m').strip()
            self.school_obj.show_grade_course()
            grade_name = input('\033[34;1m输入要选择的班级名:\033[0m').strip()
            if grade_name in self.school_obj.school_grade:
                self.school_obj.create_student(student_name, student_age, grade_name)
                self.school_db.update({self.choice_school: self.school_obj})
                print('\033[32;1m选课成功.\033[0m')
            else:
                print('\033[31;1m输入的班级名不存在.\033[0m')























