#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, shelve
from conf import config
from model import school, grade


class Manage_center(object):
    def __init__(self):
        pass

    def run(self):
        while True:
            print('1. 学校中心\n'
                  '2. 讲师中心\n'
                  '3. 学员中心\n'
                  '4. 退出')
            choice = input('>>>').strip()
            if not choice: continue
            if choice == '1':
                Manage_school()
            elif choice == '2':
                pass
            elif choice == '3':
                pass
            elif choice == '4':
                break
            else:
                print('输入错误，请重新输入.')


class Manage_school(object):
    def __init__(self):
        if os.path.exists(config.main_db_file):
            self.school_db = shelve.open(config.main_db_file, writeback=True)
            self.run_mange()
            self.school_db.close()
        else:
            self.initialize()
            self.run_mange()
            self.school_db.close()


    def initialize(self):
        self.school_db = shelve.open(config.main_db_file, writeback=True)
        self.school_db['上海'] = school.School('上海', '上海市')
        self.school_db['北京'] = school.School('北京', '北京市')

    def run_mange(self):
        while True:
            for key in self.school_db:
                print('学校名：', key)
            school_name = input('选择学校名:').strip()
            if school_name in self.school_db:
                self.school_name = school_name
                self.school_obj = self.school_db[school_name]
                while True:
                    print('1. 创建课程\n'
                          '2. 创建班级\n'
                          '3. 招聘讲师\n'
                          '4. 退出')
                    choice = input('>>>').strip()
                    if not choice: continue
                    if choice == '1':
                        self.create_course()
                    elif choice == '2':
                        self.create_grade()
                    elif choice == '3':
                        pass
                    elif choice == '4':
                        pass
                    else:
                        break

    def create_course(self):
        course_name = input('输入课程名：')
        course_price = input('输入课程价格：')
        course_time = input('输入课程周期：')
        if course_name in self.school_obj.course:
            print('课程已存在.')
            self.school_obj.create_course(course_name, course_price, course_time)
            print('课程更新完毕.')
        else:
            self.school_obj.create_course(course_name, course_price, course_time)
            print('课程添加成功.')
        self.school_db[self.school_name] = self.school_obj

    def create_grade(self):
        grade_name = input('输入班级名:').strip()
        course_name = input('输入班级要上的课程:').strip()
        if course_name in self.school_obj.course:
            course_obj = self.school_obj.course[course_name]
            if grade_name not in self.school_obj.grade:
                self.school_obj.create_grade(grade_name, course_obj)
                print('班级创建成功.')
            else:
                print('班级信息已存在.')

        else:
            print('课程不存在，请先创建课程.')

    def hire_teacher(self):
        teacher_name = input('输入讲师名:')
        teacher_price = input('输入讲师工资:')




