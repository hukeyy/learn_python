#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys
from modules.tools import file_oper
from conf.settings import school_db_file, teacher_db_file


class Teacher_center(object):
    def __init__(self):
        if os.path.exists(school_db_file):
            self.school_db = file_oper(school_db_file, 'rb')
            self.manage_run()
        else:
            print('\033[31;1m数据库不存在，请初始化数据库.')
            exit(1)
        # if not os.path.exists(teacher_db_file):
        #     self.init_teacher()
        #     self.manage_run()
        # else:
        #     self.teacher_db = file_oper(teacher_db_file, 'rb')
        #     self.manage_run()

    def init_teacher(self):
        data = {}
        file_oper(teacher_db_file, 'wb', data)

    def manage_run(self):
        for key in self.school_db:
            print('学校名：', key)
        choice_school = input('\033[34;1m输入学校名:\033[0m')
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            teacher_name = input('\033[34;1m输入讲师名:\033[0m')
            if teacher_name in self.school_obj.school_teacher:
                while True:
                    print('\n欢迎进入讲师中心\n'
                          '查看班级信息 check_grade\n'
                          '退出 exit')

                    user_func = input('>>>').strip()
                    if hasattr(self, user_func):
                        getattr(self, user_func)(teacher_name)

    def check_grade(self, teacher_name):
        self.school_obj.show_teacher_grade(teacher_name)

    def exit(self, *args):
        sys.exit('欢迎下次使用选课系统.')
