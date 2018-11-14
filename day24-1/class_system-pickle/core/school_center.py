#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys, pickle
from conf.settings import school_db_file
from modules.tools import file_oper
from modules.school import School


class School_center(object):
    def __init__(self):
        if not os.path.exists(school_db_file):
            self.init_school()
            self.school_db = file_oper(school_db_file, 'rb')
            self.manage_run()
        else:
            self.school_db = file_oper(school_db_file, 'rb')
            self.manage_run()

    def init_school(self):
        sh = School('上海', '上海市')
        bj = School('北京', '北京市')
        data = {'上海': sh, '北京': bj}
        file_oper(school_db_file, 'wb', data)

    def manage_run(self):
        for key in self.school_db:
            print('学校名：', key)

        choice_school = input('>>>').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            while True:
                print('\n欢迎进入【%s】校区\n'
                      '创建课程 add_course\n'
                      '查看课程 check_course\n'
                      '创建班级 add_grade\n'
                      '查看班级 check_grade\n'
                      '创建讲师 add_teacher\n'
                      '查看讲师 check_teacher\n'
                      '退出系统 exit' % choice_school)

                user_func = input('>>>').strip()
                if hasattr(self, user_func):
                    getattr(self, user_func)()

    def add_course(self):
        course_name = input('\033[34;1m输入课程名:\033[0m')
        course_price = input('\033[34;1m输入课程价格:\033[0m')
        course_time = input('\033[34;1m输入课程周期:\033[0m')
        if course_name not in self.school_obj.school_course:
            self.school_obj.create_course(course_name, course_price, course_time)
            self.school_db[self.choice_school] = self.school_obj
            file_oper(school_db_file, 'wb', self.school_db)
            print('\033[32;1m课程新增成功。\033[0m')
        else:
            print('\033[31;1m课程信息已存在.\033[0m')
            self.school_obj.create_course(course_name, course_price, course_time)
            print('\033[32;1m课程更新成功。\033[0m')

    def check_course(self):
        self.school_obj.show_course()

    def add_grade(self):
        grade_name = input('\033[34;1m输入班级名:\033[0m')
        course_name = input('\033[34;1m输入班级要上的课程名:\033[0m')
        if course_name in self.school_obj.school_course:
            course_obj = self.school_obj.school_course[course_name]
            if grade_name not in self.school_obj.school_grade:
                self.school_obj.create_grade(grade_name, course_obj)
                self.school_db[self.choice_school] = self.school_obj
                file_oper(school_db_file, 'wb', self.school_db)

            else:
                print('\033[31;1m班级信息已存在.\033[0m')
        else:
            print('\033[31;1m课程信息不存在.\033[0m')

    def check_grade(self):
        self.school_obj.show_grade()

    def add_teacher(self):
        teacher_name = input('\033[34;1m输入讲师名:\033[0m')
        teacher_salary = input('\033[34;1m输入讲师薪资:\033[0m')
        grade_name = input('\033[34;1m输入讲师关联的班级:\033[0m')
        if grade_name in self.school_obj.school_grade:
            grade_obj = self.school_obj.school_grade[grade_name]
            if teacher_name not in self.school_obj.school_teacher:
                self.school_obj.create_teacher(teacher_name, teacher_salary, grade_name, grade_obj)
                print('\033[32;1m讲师新增成功.\033[0m')
            else:
                print('\033[31;1m讲师信息已存在.\033[0m')
                self.school_obj.create_teacher(teacher_name, teacher_salary, grade_name, grade_obj)
                print('\033[32;1m讲师更新成功.\033[0m')
            self.school_db[self.choice_school] = self.school_obj
            file_oper(school_db_file, 'wb', self.school_db)
        else:
            print('\033[31;1m班级信息不存在，请先创建班级.\033[0m')

    def check_teacher(self):
        self.school_obj.show_teacher()

    def exit(self, *args):
        sys.exit('欢迎下次使用选课系统.')
