#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, pickle
from model.school import School
from core.file_oper import file_oper, options
from conf import settings
from model.course import Course


class Manage_school(object):
    def __init__(self):
        if not os.path.exists(settings.db_main_file):
            self.init_database()
            self.school_db = {self.sh:{}, self.bj:{}}
            file_oper(settings.db_main_file, 'wb', self.school_db)
        else:
            self.school_db = file_oper(settings.db_main_file, 'rb')


    def init_database(self):
        self.sh = School('上海', '上海市')
        self.bj = School('北京', '北京市')

    def run_manage(self):
        flag = True
        self.db_main = dict()
        while flag:
            for key in self.school_db:
                key.cat_school()
                self.db_main[key.name] = key
            school_name = input('\033[34;1m请选择学校名：\033[0m').strip()
            if not school_name: continue
            if school_name in self.db_main:
                print('\033[33;1m欢迎进入【%s】学校\033[0m'.center(50, '#') % school_name)
                self.school = self.db_main[school_name]
                while flag:
                    choice = options(settings.school_list)
                    # school_list = ['创建课程', '招聘讲师', '创建班级', '退出']
                    if choice == '1':
                        print('\033[32;1m创建课程\033[0m')
                        self.course_db = self.school_db[self.school]
                        if self.course_db:
                            print('\033[33;1m目前【%s】已有课程\033[0m'.center(50, '#') % school_name)
                            for key in self.course_db:
                                key.cat_course()
                        else:
                            print('\033[32;1m目前【%s】学校没有课程.\033[0m' % school_name)
                        course_name = input('\033[34;1m课程名：\033[0m').strip()


                    elif choice == '2':
                        print('\033[32;1m招聘讲师\033[0m')
                    elif choice == '3':
                        print('\033[32;1m创建班级\033[0m')
                    elif choice == '4':
                        flag = False
                    else:
                        print('\033[31;1m错误：序号错误.\033[0m')

            else:
                print('\033[31;1m错误：学校信息不存在.\033[0m')

































