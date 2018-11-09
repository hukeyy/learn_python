#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, shelve, sys
from conf.settings import main_db_file
from modules.school import School

class Manage_center(object):
    def __init__(self):
        pass
    def run(self):
        while True:
            print('1. 学校中心\n'
                  '2. 讲师中心\n'
                  '3. 学生中心\n'
                  '4. 退出')
            user_choice = input('>>>').strip()
            if user_choice == '1':
                Manage_school()
            elif user_choice == '2':
                Manage_teacher()
                pass
            elif user_choice == '3':
                Manage_student()
                pass
            elif user_choice == '4':
                break
            else:
                print('\033[31;1m输入错误，请重新输入.\033[0m')


class Manage_school(object):
    def __init__(self):
        if not os.path.exists(main_db_file+'.dat'):
            self.init_school()
            self.manage_run()
            self.school_db.close()
        else:
            self.school_db = shelve.open(main_db_file)
            print(self.school_db['上海'])
            self.manage_run()
            self.school_db.close()

    def init_school(self):
        self.school_db = shelve.open(main_db_file)
        self.school_db['上海'] = School('上海', '上海市')
        self.school_db['北京'] = School('北京', '北京市')

    def manage_run(self):
        for key in self.school_db:
            print('学校名:', key)

        choice_school = input('\033[34;1m选择学校名:\033[0m')
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            while True:
                print('\n欢迎进入【%s】学区\n'
                      '新增课程 add_course\n'
                      '查看课程 check_course\n'
                      '新增班级 add_grade\n'
                      '查看班级 check_grade\n'
                      '新增讲师 add_teacher\n'
                      '查看讲师 check_teacher\n'
                      '退出 exit' % choice_school)
                user_choice = input('>>>').strip()
                if hasattr(self, user_choice):
                    getattr(self, user_choice)()
        else:
            print('\033[31;1m输入的学校名不存在，请重新输入.\033[0m')

    def add_course(self):
        course_name = input('\033[34;1m输入课程名:\033[0m').strip()
        course_price = input('\033[34;1m输入课程价格:\033[0m').strip()
        course_time = input('\033[34;1m输入课程周期:\033[0m').strip()
        if course_name not in self.school_obj.school_course:
            self.school_obj.create_course(course_name, course_price, course_time)
            print('\033[32;1m课程新增成功。\033[0m')
        else:
            print('\033[31;1m课程已存在。\033[0m')
            self.school_obj.create_course(course_name, course_price, course_time)
            print('\033[32;1m课程更新成功。\033[0m')
        self.school_db.update({self.choice_school: self.school_obj})

    def check_course(self):
        self.school_obj.show_course()

    def add_grade(self):
        grade_name = input('\033[34;1m输入班级名:\033[0m').strip()
        course_name = input('\033[34;1m输入班级关联的课程名:\033[0m').strip()
        if grade_name not in self.school_obj.school_grade:
            if course_name in self.school_obj.school_course:
                course_obj = self.school_obj.school_course[course_name]
                self.school_obj.create_grade(grade_name, course_obj)
                print('\033[32;1m班级添加成功.\033[0m')
            else:
                print('\033[31;1m课程信息不存在，请先创建课程信息.\033[0m')
        else:
            print('\033[31;1m班级信息已存在.')
        self.school_db.update({self.choice_school: self.school_obj})

    def check_grade(self):
        self.school_obj.show_grade()

    def add_teacher(self):
        teacher_name = input('\033[34;1m输入讲师名:\033[0m').strip()
        teacher_salary = input('\033[34;1m输入讲师薪资:\033[0m').strip()
        teacher_grade = input('\033[34;1m输入讲师关联的班级名:\033[0m').strip()
        if teacher_grade in self.school_obj.school_grade:
            grade_obj = self.school_obj.school_grade[teacher_grade]
            if teacher_name not in self.school_obj.school_teacher:
                self.school_obj.create_teacher(teacher_name, teacher_salary,
                                               teacher_grade, grade_obj)
                print('\033[32;1m讲师新增成功\033[0m')
            else:
                print('\033[31;1m讲师信息已存在.\033[0m')
                self.school_obj.update_teacher(teacher_name,
                                               teacher_grade, grade_obj)
                print('\033[32;1m讲师信息更新成功\033[0m')
            self.school_db.update({self.choice_school: self.school_obj})
        else:
            print('\033[31;1m系统错误：关联的班级不存在.\033[0m')


    def check_teacher(self):
        self.school_obj.show_teacher()


    def exit(self):
        self.school_db.close()
        sys.exit('欢迎再次使用选课系统。')

class Manage_teacher(object):
    def __init__(self):
        if os.path.exists(main_db_file + '.dat'):
            self.school_db = shelve.open(main_db_file)
            self.manage_run()
            self.school_db.close()

    def manage_run(self):
        for key in self.school_db:
            print('\033[32;1m学校名称:\033[0m', key)
        choice_school = input('\033[34;1m输入选择学校:\033[0m').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            teacher_name = input('\033[34;1m输入讲师名:\033[0m').strip()
            while True:
                if teacher_name in self.school_obj.school_teacher:
                    print('\n欢迎来到讲师中心\n'
                          '查看班级 check_grade\n'
                          '退出程序 exit')
                    user_func = input('>>>').strip()
                    if hasattr(self, user_func):
                        getattr(self, user_func)(teacher_name)
        else:
            print('\033[31;1m选择的学校名不存在.\033[0m')

    def check_grade(self, teacher_name):
        self.school_obj.show_teacher_gradeinfo(teacher_name)

    def exit(self, *args):
        sys.exit('欢迎下次使用选课系统')


class Manage_student(object):
    def __init__(self):
        if os.path.exists(main_db_file + '.dat'):
            self.school_db = shelve.open(main_db_file)
            self.run_mange()
            self.school_db.close()

        else:
            print('\033[31;1m数据库文件不存在，请先创建学校\033[0m')
            exit()

    def run_mange(self):
        print('\n欢迎进入学员中心')
        for key in self.school_db:
            print('学校名称:', key)
        choice_school = input('\033[34;1m输入选择注册的学校名:\033[0m').strip()
        if choice_school in self.school_db:
            self.choice_school = choice_school
            self.school_obj = self.school_db[choice_school]
            student_name = input('\033[34;1m输入学生的姓名:\033[0m')
            student_age = input('\033[34;1m输入学生的年龄:\033[0m')
            self.school_obj.show_grade_course()
            grade_name = input('\033[34;1m选择要上课的班级名:\033[0m').strip()
            if grade_name in self.school_obj.school_grade:
                self.school_obj.create_student(student_name, student_age, grade_name)
                self.school_db.update({self.choice_school: self.school_obj})
                print('\033[32;1m学生注册成功.\033[0m')
            else:
                print('\033[31;1m输入的班级不存在，请先创建班级信息.\033[0m')

        else:
            print('\033[31;1m输入的学校名不存在，请重新输入.\033[0m')





























