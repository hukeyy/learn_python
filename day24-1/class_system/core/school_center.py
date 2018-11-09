#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys, shelve
from conf.settings import main_file_db
from modules.school import School


class School_center(object):
    def __init__(self):
        if not os.path.exists(main_file_db):
            self.init_school()
            self.mange_run()
            self.school_db.close()
        else:
            self.school_db = shelve.open(main_file_db)
            self.mange_run()
            self.school_db.close()

    def init_school(self):
        self.school_db = shelve.open(main_file_db)
        self.school_db['北京'] = School('北京', '北京市')
        self.school_db['上海'] = School('上海', '上海市')

    def mange_run(self):
        for key in self.school_db:
            print('学校名:', key)
        choice_school = input('\033[34;1m选择学校名:\033[0m').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            while True:
                print('\n欢迎进入【%s】学区\n'
                      '创建课程 add_course\n'
                      '查看课程 check_course\n'
                      '创建班级 add_grade\n'
                      '查看班级 check_grade\n'
                      '招聘讲师 add_teacher\n'
                      '查看讲师 check_teacher\n'
                      '退出 exit' % choice_school)

                user_choice = input('>>>').strip()

                if hasattr(self, user_choice):
                    getattr(self, user_choice)()

    def add_course(self):
        course_name = input('\033[34;1m输入课程名:\033[0m')
        course_price = input('\033[34;1m输入课程价格:\033[0m')
        course_time = input('\033[34;1m输入课程周期:\033[0m')
        if course_name not in self.school_obj.school_course:
            self.school_obj.create_course(course_name, course_price, course_time)
            print('\033[32;1m课程新增成功.\033[0m')
        else:
            print('\033[31;1m课程信息已存在.\033[0m')
            self.school_obj.create_course(course_name, course_price, course_time)
            print('课程更新成功.')
        self.school_db.update({self.choice_school: self.school_obj})

    def check_course(self):
        self.school_obj.show_course()

    def add_grade(self):
        grade_name = input('\033[34;1m输入班级名:\033[0m')
        grade_course = input('\033[34;1m输入班级要上的课程名:\033[0m')
        if grade_name not in self.school_obj.school_grade:
            if grade_course in self.school_obj.school_course:
                course_obj = self.school_obj.school_course[grade_course]

            else:
                print('\033[31;1m课程信息不存在，请先创建课程信息.\033[0m')

        else:
            print('\033[31;1m班级信息已存在.\033[0m')

    def check_grade(self):
        pass

    def exit(self, *args):
        sys.exit('欢迎下次使用选课系统.')
























