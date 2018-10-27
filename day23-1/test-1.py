#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

__db_main = os.path.join(BASE_DIR, 'school_dict')
__db_teacher = os.path.join(BASE_DIR, 'teacher_dict')


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def cat_school(self):
        print('\033[32;1m学校【%s】\t地址【%s】\033[0m' % (self.name, self.addr))

    def create_course(self, main_db, course, main_file):
        main_db[self][course] = {}
        file_oper(main_file, 'wb', main_db)

    def hire_teacher(self, main_db, course, teacher, main_file):
        main_db[self][course] = {'teacher': teacher}
        file_oper(main_file, 'wb', main_db)

    def create_grade(self, main_db, teacher_db, course, teacher, grade, main_file, teacher_file):
        main_db[self][course]['grade'] = grade
        file_oper(main_file, 'wb', main_db)
        teacher_db[teacher] = {'grade': grade}
        file_oper(teacher_file, 'wb', teacher_db)


class Course(object):
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time

    def cat_course(self):
        print('\033[32;1m课程【%s】\t价格【%s元】\t周期【%s个月】\033[0m' % (self.name, self.price, self.time))


class Teacher(object):
    def __init__(self, name, age, school, course, role='讲师'):
        self.name = name
        self.age = age
        self.school = school
        self.course = course
        self.role = role

    def cat_teacher(self):
        print('\033[32;1m课程【%s】\t讲师【%s】\033[0m' % (self.course, self.name))


class Grade(object):
    def __init__(self, name, course, teacher):
        self.name = name
        self.course = course
        self.teacher = teacher
        self.student = set([])

    def cat_grade(self):
        print('\033[32;1m课程【%s】\t讲师【%s】\t班级【%s】\033[0m' % (self.course, self.teacher, self.name))

    def add_student(self, teacher_db, teacher, student_name, teahcer_file):
        self.student.add(student_name)
        teacher_db[teacher] = {'grade': self}
        file_oper(teahcer_file, 'wb', teacher_db)


def file_oper(file, mode, *args):
    if mode == 'wb':
        data = args[0]
        with open(file, mode) as f:
            pickle.dump(data, f)
    elif mode == 'rb':
        with open(file, mode) as f:
            data = pickle.load(f)
            return data


def init_database():
    sh = School('上海', '上海市')
    bj = School('北京', '北京市')
    if not os.path.exists(__db_main):
        data = {sh: {}, bj: {}}
        file_oper(__db_main, 'wb', data)

    if not os.path.exists(__db_teacher):
        data = {}
        file_oper(__db_teacher, 'wb', data)


def options(li):
    for i, k in enumerate(li):
        print(i + 1, k)
    choice = input('>>>').strip()
    return choice


def information(db, mode, *args):
    if args:
        dict_info, set_info = {}, args[0]
    else:
        dict_info, set_info = {}, set([])

    if db:
        for key in db:
            if mode == 'main':
                key.cat_school()
            elif mode == 'course':
                key.cat_course()
            elif mode == 'teacher' and key == 'teacher':
                db[key].cat_teacher()
                set_info.add(db[key].name)
            elif mode == 'grade' and key == 'grade':
                db[key].cat_grade()
                set_info.add(db[key].name)
            if not isinstance(key, str):
                dict_info[key.name] = key

    return dict_info, set_info


def school_center():
    print('\033[33;1m【school_center】\033[0m')
    Flag = True
    while Flag:
        main_db = file_oper(__db_main, 'rb')
        res_school = information(main_db, 'main')[0]
        school_name = input('\033[34;1m输入学校名:\033[0m').strip()
        if school_name in res_school:
            school = res_school[school_name]
            while Flag:
                print('\033[33;1m欢迎进入【%s】学校\033[0m' % school_name)
                choice = options(school_list)
                if choice == '1':
                    while True:
                        print('\033[33;1m学校【%s】目前已有课程信息\033[0m' % school_name)
                        res_course = information(main_db[school], 'course')[0]
                        if_cont = input('\033[34;1m是否创建课程信息[y/b]:\033[0m').strip()
                        if if_cont == 'y':
                            course_name = input('\033[34;1m输入课程名:\033[0m').strip()
                            if course_name not in res_course:
                                course_price = input('\033[34;1m输入课程价格:\033[0m').strip()
                                course_time = input('\033[34;1m输入课程周期:\033[0m').strip()
                                course = Course(course_name, course_price, course_time)
                                school.create_course(main_db, course, __db_main)
                        elif if_cont == 'b':
                            break
                        else:
                            print('\033[31;1m课程信息已存在.\033[0m')

                elif choice == '2':
                    while True:
                        res_course = information(main_db[school], 'None')[0]
                        print('\033[33;1m学校【%s】目前已有讲师信息\033[0m' % school_name)
                        if res_course:
                            for i in res_course:
                                k = res_course[i]
                                res_teacher = information(main_db[school][k], 'teacher')[1]
                                if not res_teacher:
                                    print('\033[31;1m课程【%s】\t讲师【None】\033[0m' % k.name)
                        if_cont = input('\033[34;1m是否招聘讲师信息[y/b]:\033[0m').strip()
                        if if_cont == 'y':
                            teacher_name = input('\033[34;1m输入讲师名:\033[0m').strip()
                            teacher_age = input('\033[34;1m输入讲师年龄:\033[0m').strip()
                            course_name = input('\033[34;1m输入讲师要上的课程:\033[0m').strip()
                            if course_name in res_course:
                                course = res_course[course_name]
                                if teacher_name not in res_teacher:
                                    teacher = Teacher(teacher_name, teacher_age, school_name, course_name)
                                    school.hire_teacher(main_db, course, teacher, __db_main)

                            else:
                                print('\033[31;1m输入的课程不存在，请先创建课程.\033[0m')

                        elif if_cont == 'b':
                            break
                        else:
                            print('\033[31;1m输入错误，请重新输入.\033[0m')

                elif choice == '3':
                    while True:
                        teacher_db = file_oper(__db_teacher, 'rb')
                        res_course = information(main_db[school], 'None')[0]
                        print('\033[33;1m学校【%s】目前已有班级信息\033[0m' % school_name)
                        if res_course:
                            for i in res_course:
                                k = res_course[i]
                                res_grade = information(main_db[school][k], 'grade')[1]
                                if not res_grade:
                                    print('\033[31;1m目前没有班级信息.\033[0m')
                        if_cont = input('\033[34;1m是否创建班级信息[y/b]:\033[0m').strip()
                        if if_cont == 'y':
                            grade_name = input('\033[34;1m输入班级名:\033[0m').strip()
                            course_name = input('\033[34;1m输入班级要上的课程:\033[0m').strip()
                            if course_name in res_course:
                                course = res_course[course_name]
                                if main_db[school][course]:
                                    teacher = main_db[school][course]['teacher']
                                    if grade_name not in res_grade:
                                        grade = Grade(grade_name, course_name, teacher.name)
                                        school.create_grade(main_db, teacher_db, course, teacher, grade,
                                                            __db_main, __db_teacher)
                                    else:
                                        print('\033[31;1m班级信息已存在.\033[0m')

                                else:
                                    print('\033[31;1m讲师信息不存在，请先创建讲师.\033[0m')
                            else:
                                print('\033[31;1m输入的课程信息不存在，请重新输入.\033[0m')
                        else:
                            break
                elif choice == '4':
                    Flag = False
                else:
                    print('\033[31;1m输入错误，请重新输入.\033[0m')

        else:
            print('\033[31;1m输入错误，请重新输入.\033[0m')


def teacher_center():
    print('\033[33;1m【teacher_center】\033[0m')
    teacher_db = file_oper(__db_teacher, 'rb')
    teacher_name = input('\033[34;1m输入讲师名:\033[0m').strip()
    res_teacher = information(teacher_db, 'None')[0]
    if res_teacher:
        if teacher_name in res_teacher:
            teacher = res_teacher[teacher_name]
            grade = teacher_db[teacher].get('grade')
            while True:
                choice = options(teacher_list)
                if choice == '1':
                    print('\033[32;1m学校【%s】\t班级【%s】\033[0m' % (teacher.school, grade.name))
                    any = input('输入任意键退出当前:')
                elif choice == '2':
                    print('\033[32;1m班级【%s】\t学员【%s】\033[0m' % (grade.name, grade.student))
                    any = input('输入任意键退出当前:')
                elif choice == '3':
                    break
                else:
                    print('\033[31;1m输入错误，请重新输入.\033[0m')
    else:
        print('\033[31;1m没有讲师信息，请先创建讲师信息.\033[0m')


def student_center():
    print('\033[33;1m【student_center】\033[0m')
    while True:
        choice = options(student_list)
        main_db = file_oper(__db_main, 'rb')
        teacher_db = file_oper(__db_teacher, 'rb')
        if choice == '1':
            student_name = input('\033[34;1m输入学员姓名:\033[0m').strip()
            res_school = information(main_db, 'main')[0]
            school_name = input('\033[34;1m选择学校名:\033[0m').strip()
            if school_name in res_school:
                school = res_school[school_name]
                res_course = information(main_db[school], 'course')[0]
                course_name = input('\033[34;1m选择课程:\033[0m').strip()
                if course_name in res_course:
                    course = res_course[course_name]
                    if main_db[school][course].get('grade'):
                        for i in teacher_db:
                            if i.course == course.name:
                                teacher = i
                                grade = teacher_db[teacher]['grade']
                        print('\033[32;1m课程【%s】的价格【%s】\033[0m' % (course.name, course.price))
                        if_pay = input('\033[34;1m是否支付当前费用[y]:\033[0m').strip()
                        if if_pay == 'y':
                            grade.student.add(student_name)
                            grade.add_student(teacher_db, teacher, student_name, __db_teacher)
                            print('\033[32;1m选课成功.\033[0m')
                            any = input('输入任意键退出当前:')
                        else:
                            break

                    else:
                        print('\033[31;1m讲师信息不存在，请先招聘讲师.\033[0m')
                else:
                    print('\033[31;1m输入的课程不存在.\033[0m')
            else:
                print('\033[31;1m输入的学校名不存在.\033[0m')

        elif choice == '2':
            break
        else:
            print('\033[31;1m输入错误，请重新输入.\033[0m')


def start():
    while True:
        choice = options(main_list)
        if choice == '1':  # 学校中心
            school_center()
        elif choice == '2':  # 课程中心
            teacher_center()
        elif choice == '3':  # 讲师中心
            student_center()
        elif choice == '4':  # 退出
            break
        else:
            print('\033[31;1m输入错误，请重新输入.\033[0m')


if __name__ == '__main__':
    init_database()
    main_list = ['学校中心', '讲师中心', '学生中心', '退出']
    school_list = ['创建课程', '招聘讲师', '创建班级', '返回']
    teacher_list = ['查看班级信息', '查看班级学员列表', '返回']
    student_list = ['学员注册', '返回']
    start()
