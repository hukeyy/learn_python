#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
from core.file_oper import file_oper

class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def cat_school(self):
        print('\033[32;1m学校名：【%s】地址：【%s】\033[0m' % (self.name, self.addr))

    def create_course(self, db_main, course, file):
        '''创建课程'''
        db_main[self][course] = {}
        file_oper(file, 'wb', db_main)

    def hire_teacher(self, db_main, course, teacher, file):
        db_main[self][course] = {'teacher': teacher}
        file_oper(file, 'wb', db_main)

    def create_grade(self, db_main, db_teacher, course, teacher, grade, file1, file2):
        db_main[self][course]['grade'] = grade
        file_oper(file1, 'wb', db_main)
        db_teacher[teacher] = {'grade': grade}
        file_oper(file2, 'wb', db_teacher)
