#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import os
from core.file_oper import file_oper, options
from conf import settings
from model import school, course, teacher, grade


class Manage_school(object):
    def __init__(self):
        self.db_school = dict()
        self.course_dict = dict()
        self.set_teacher = set([])
        if not os.path.exists(settings.db_main_file):
            self.init_database()
            self.school_db = {self.sh: {}, self.bj: {}}
            file_oper(settings.db_main_file, 'wb', self.school_db)
        else:
            self.school_db = file_oper(settings.db_main_file, 'rb')

        if not os.path.exists(settings.db_teacher_file):
            self.teacher_db = {}
            file_oper(settings.db_teacher_file, 'wb', self.teacher_db)
        else:
            self.teacher_db = file_oper(settings.db_teacher_file, 'rb')

    def init_database(self):
        self.sh = school.School('上海', '上海市')
        self.bj = school.School('北京', '北京市')

    def run_manage(self):
        flag = True
        while flag:
            for key in self.school_db:
                key.cat_school()
                self.db_school[key.name] = key
            school_name = input('\033[34;1m请选择学校名：\033[0m').strip()
            if not school_name: continue
            if school_name in self.db_school:
                print('\033[33;1m欢迎进入【%s】学校\033[0m'.center(50, '#') % school_name)
                self.school = self.db_school[school_name]
                while flag:
                    choice = options(settings.school_list)
                    if choice == '1':
                        while True:
                            course_db = self.school_db[self.school]
                            if course_db:
                                print('\033[33;1m目前【%s】已有课程\033[0m'.center(50, '#') % school_name)
                                for key in course_db:
                                    key.cat_course()
                                    self.course_dict[key.name] = key
                            else:
                                print('\033[32;1m目前【%s】学校没有课程.\033[0m' % school_name)
                            if_cont = input('\033[34;1m是否创建课程【y】创建【b】返回:\033[0m').strip()
                            if if_cont == 'y':
                                course_name = input('\033[34;1m课程名：\033[0m').strip()
                                if course_name not in self.course_dict:
                                    course_price = input('\033[34;1m课程【%s】的价格：\033[0m' % course_name).strip()
                                    course_time = input('\033[34;1m课程【%s】的周期：\033[0m' % course_name).strip()
                                    s_course = course.Course(course_name, course_price, course_time)
                                    self.school.create_course(self.school_db, s_course, settings.db_main_file)
                                    print('\033[32;1m课程【%s】创建成功.\033[0m' % course_name)
                                else:
                                    print('\033[31;1m错误：课程已存在.\033[0m')
                            elif if_cont == 'b':
                                break

                    elif choice == '2':
                        print('\033[32;1m招聘讲师\033[0m')
                        # course_dict = dict()
                        # set_teacher = set([])
                        while True:
                            print('\033[33;1m学校【%s】目前已有课程及讲师\033[0m'.center(50, '#') % school_name)
                            course_db = self.school_db[self.school]
                            for i in course_db:
                                self.course_dict[i.name] = i
                                k = course_db[i]
                                teacher_db = k.get('teacher')
                                if teacher_db:
                                    self.set_teacher.add(teacher_db.name)
                                    teacher_db.cat_teacher()
                                else:
                                    print('\033[31;1m课程：【%s】\t讲师：【None】\033[0m' % i.name)
                            if_cont = input('\033[34;1m是否招聘讲师【y】招聘【b】返回\033[0m').strip()
                            if if_cont == 'y':
                                teacher_name = input('\033[34;1m输入要招聘讲师的名字:\033[0m').strip()
                                course_name = input('\033[34;1m输入讲师要教授的课程：\033[0m').strip()
                                if course_name in self.course_dict:
                                    course_db = self.course_dict[course_name]
                                    if teacher_name not in self.set_teacher:
                                        teacher_db = teacher.Teacher(teacher_name, school_name, course_name)
                                        self.school.hire_teacher(self.school_db, course_db,
                                                                 teacher_db, settings.db_main_file)
                                    else:
                                        print('\033[31;1m错误：讲师信息已存在。\033[0m')


                                else:
                                    print('\033[31;1m错误：课程信息不存在，请先创建课程.\033[0m')

                            elif if_cont == 'b':
                                break

                    elif choice == '3':
                        print('\033[32;1m创建班级\033[0m')
                        course_dict = dict()
                        set_grade = set([])
                        set_teacher = set([])
                        while True:
                            print('\033[33;1m学校【%s】目前已有的班级\033[0m'.center(50, '#') % school_name)
                            course_db = self.school_db[self.school]
                            if course_db:
                                for i in course_db:
                                    course_dict[i.name] = i
                                    k = course_db[i]
                                    grade_db = k.get('grade')
                                    if grade_db:
                                        set_grade.add(grade_db.name)
                                        grade_db.cat_grade()
                                    # else:
                                    #     print('\033[31;1m目前【%s】学校未创建班级\033[0m'.center(50, '#') % school_name)
                            else:
                                print('\033[31;1m错误：课程信息不存在，请先创建课程.\033[0m')

                            if_cont = input('\033[034;1m是否创建班级【y】创建【b】退出:\033[0m').strip()
                            if if_cont == 'y':
                                grade_name = input('\033[34;1m输入班级名:\033[0m').strip()
                                course_name = input('\033[34;1m输入班级要上的课程：\033[0m').strip()
                                if course_name in course_dict:
                                    course_db = course_dict[course_name]
                                    if self.school_db[self.school][course_db]:
                                        teacher_db = self.school_db[self.school][course_db]['teacher']
                                        if grade_name not in set_grade:
                                            grade_db = grade.Grade(grade_name, course_name, teacher_db.name)
                                            self.school.create_grade(self.school_db, self.teacher_db, course_db,
                                                                     teacher_db, grade_db, settings.db_main_file,
                                                                     settings.db_teacher_file)

                                        else:
                                            print('\033[31;1m错误：班级信息不存在.\033[0m')
                                    else:
                                        print('\033[31;1m错误：讲师信息不存在.\033[0m')

                                else:
                                    print('\033[31;1m错误：当前课程没有讲师信息.\033[0m')


                            elif if_cont == 'b':
                                break

                    elif choice == '4':
                        flag = False
                    else:
                        print('\033[31;1m错误：序号错误.\033[0m')

            else:
                print('\033[31;1m错误：学校信息不存在.\033[0m')
