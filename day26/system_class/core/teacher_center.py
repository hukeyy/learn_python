#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, shelve, sys
from conf.settings import school_file_db


class Teacher_center(object):
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
            teacher_name = input('\033[32;1m输入讲师名:\033[0m').strip()
            if teacher_name in self.school_obj.school_teacher:
                while True:
                    print('\n欢迎来到讲师中心\n'
                          '查看班级信息 check_grade\n'
                          '退出系统 exit')
                    user_func = input('>>>').strip()
                    if hasattr(self, user_func):
                        getattr(self, user_func)(teacher_name)
            else:
                print('\033[31;1m讲师信息不存在.\033[0m')

    def check_grade(self, teacher_name):
        self.school_obj.show_grade_student(teacher_name)

    def exit(self, *args):
        self.school_db.close()
        sys.exit('欢迎下次使用选课系统.')

















