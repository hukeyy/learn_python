#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, shelve, sys
from conf.settings import school_db_file

class Teacher_center(object):
    def __init__(self):
        if os.path.exists(school_db_file + '.dat'):
            self.school_db = shelve.open(school_db_file)
            self.mange_run()
            self.school_db.close()
        else:
            print('\033[31;1m数据库文件不存在，请先初始化数据库.\033[0m')

    def mange_run(self):
        for key in self.school_db:
            print('学校名：', key)
        choice_school = input('\033[34;1m输入学校名:\033[0m').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            teacher_name = input('\033[34;1m输入讲师名:\033[0m')
            while True:
                if teacher_name in self.school_obj.school_teacher:
                    print('\n欢迎来到教师中心\n'
                          '查看班级 check_grade\n'
                          '退出程序 exit')
                    user_func = input('>>>').strip()
                    if hasattr(self, user_func):
                        getattr(self, user_func)(teacher_name)
                else:
                    print('\033[31;1m讲师信息不存在.\033[0m')

    def check_grade(self, teacher_name):
        self.school_obj.show_teacher_grade(teacher_name)

    def exit(self, *args):
        sys.exit('欢迎下次登录选课系统.')
