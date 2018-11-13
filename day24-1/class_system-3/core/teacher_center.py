#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys, shelve
from conf.settings import school_db_file


class Teacher_center(object):
    def __init__(self):
        if os.path.exists(school_db_file + '.dat'):
            self.school_db = shelve.open(school_db_file)
            self.manage_run()
            self.school_db.close()
        else:
            print('\033[31;1m数据库文件不存在，请先初始化.\033[0m')
            exit(1)

    def manage_run(self):
        for key in self.school_db:
            print('学校名：', key)
        choice_school = input('>>>').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            teacher_name = input('\033[34;1m输入讲师名:\033[0m')
            if teacher_name in self.school_obj.school_teacher:
                while True:
                    print('查看班级信息 check_grade\n'
                          '退出系统 exit\n')
                    user_func = input('>>>').strip()
                    if hasattr(self, user_func):
                        getattr(self, user_func)(teacher_name)
            else:
                print('\033[31;1m讲师信息不存在.\033[0m')

        else:
            print('\033[31;1m输入的学校名不存在.\033[0m')

    def check_grade(self, teacher_name):
        self.school_obj.check_teacher_grade(teacher_name)

    def exit(self, *args):
        self.school_db.close()
        sys.exit('欢迎下次使用选课系统.')


























