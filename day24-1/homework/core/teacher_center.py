#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os
from conf.settings import main_db_file, teacher_db_file
from model.tools import option, file_oper


class Teacher_center(object):
    teacher_list = ['查看班级信息', '查看班级学员列表', '返回']

    def __init__(self):
        self.school_db = file_oper(main_db_file, 'rb')
        self.teacher_db = file_oper(teacher_db_file, 'rb')
        self.run()

    def run(self):
        for key in self.school_db:
            print('学校名【%s】' % key)
        school_name = input('\033[34;1m输入学校名:\033[0m')
        self.school = self.school_db[school_name]
        teacher_name = input('\033[34;1m输入讲师名:\033[0m')
        if teacher_name in self.school.school_teacher and teacher_name in self.school.school_teacher:
            self.teacher = self.school.school_teacher[teacher_name]
            print('\033[33;1m欢迎进入【%s】讲师管理中心\033[0m' % teacher_name)
            while True:
                choice = option(Teacher_center.teacher_list)
                if choice == '1':
                    self.cat_grade()
                elif choice == '2':
                    self.cat_student()
                else:
                    break
        else:
            print('\033[31;1m错误：讲师信息不存在.\033[0m')

    def cat_grade(self):
        for grade_name in self.teacher.teacher_grade:
            print('\033[32;1m课程【%s】\033[0m' % grade_name)
    def cat_student(self):
        print('2')
        for grade_name in self.teacher.teacher_grade:
            grade = self.teacher.teacher_grade[grade_name]
            print('学员信息：')
            for student in grade.grade_student:
                print('\033[32;1m%s\033[0m' % student)


