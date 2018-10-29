#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
__db_main = os.path.join(BASE_DIR, 'main_dict')  # 学校内容文件
__db_teacher = os.path.join(BASE_DIR, 'teacher_dict')  # 讲师课程内容文件


class School(object):
    '''学校类'''

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

    def create_grade(self, main_db, teacher_db, course, grade, teacher, main_file, teacher_file):
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
    def __init__(self, name, age, school, course):
        self.name = name
        self.age = age
        self.school = school
        self.course = course

    def cat_teacher(self):
        print('\033[32;1m课程【%s】\t讲师【%s】\033[0m' % (self.course, self.name))


class Grade(object):
    def __init__(self, name, course, teacher):
        self.name = name
        self.course = course
        self.teacher = teacher
        self.student = set([])

    def cat_grade(self):
        print('\033[32;1m课程【%s】\t班级【%s】\033[0m' % (self.course, self.name))

    def add_student(self, teacher_db, teacher, student_name, teacher_file):
        self.student.add(student_name)
        teacher_db[teacher] = {'grade': self}
        file_oper(teacher_file, 'wb', teacher_db)


def options(li):
    '''序号和标题循环打印，返回选择序号'''
    for i, k in enumerate(li):
        print(i + 1, k)
    choice = input('>>>').strip()
    return choice


def information(db, mode):
    set_info = set()
    dict_info = {}
    if db:
        for key in db:
            if mode == 'main':
                key.cat_school()
            elif mode == 'course':
                key.cat_course()
            elif mode == 'teacher' and key == 'teacher':
                db[key].cat_teacher()
                set_info.add(key)
            elif mode == 'grade' and key == 'grade':
                db[key].cat_grade()
                set_info.add(key)
            if not isinstance(key, str):
                dict_info[key.name] = key

    return dict_info, set_info


def school_center():
    Flag = True
    while Flag:
        main_db = file_oper(__db_main, 'rb')
        res_school = information(main_db, 'main')[0]
        school_name = input('\033[34;1m选择学校名:\033[0m')
        if school_name in res_school:
            school = res_school[school_name]
            while Flag:
                choice = options(school_list)
                if choice == '1':  # 创建课程
                    while True:
                        print('\033[33;1m目前学校【%s】已经存在的课程信息:\033[0m' % school_name)
                        res_course = information(main_db[school], 'course')[0]
                        print(type(res_course))
                        if not res_course:
                            print('\033[31;1m目前没有任何课程信息.\033[0m')
                        if_cont = input('\033[34;1m是否创建课程[y/b]:\033[0m').strip()
                        if if_cont == 'y':
                            course_name = input('\033[34;1m输入课程名:').strip()
                            if course_name not in res_course:
                                course_price = input('\033[34;1m输入课程价格:').strip()
                                course_time = input('\033[34;1m输入课程周期:').strip()
                                course = Course(course_name, course_price, course_time)
                                school.create_course(main_db, course, __db_main)

                            else:
                                print('\033[31;1m该课程名已存在.\033[0m')
                        elif if_cont == 'b':
                            break
                        else:
                            print('\033[31;1m输入错误，请重新输入.\033[0m')

                elif choice == '2':  # 招聘讲师
                    while True:
                        print('\033[33;1m目前学校【%s】已经存在的讲师信息:\033[0m' % school_name)
                        res_course = information(main_db[school], 'None')[0]
                        if res_course:
                            for i in res_course:
                                k = res_course[i]
                                res_teacher = information(main_db[school][k], 'teacher')[1]
                                print(main_db)
                                if not res_teacher:
                                    print('\033[31;1m课程【%s】\t讲师【None】\033[0m' % k.name)
                        if_cont = input('\033[34;1m是否招聘讲师[y/b]:\033[0m').strip()
                        if if_cont == 'y':
                            teacher_name = input('\033[34;1m输入讲师名:').strip()
                            teacher_age = input('\033[34;1m输入讲师年龄:').strip()
                            course_name = input('\033[34;1m输入课程名:').strip()
                            if course_name in res_course:
                                course = res_course[course_name]
                                if teacher_name not in res_teacher:
                                    teacher = Teacher(teacher_name, teacher_age, school_name, course_name)
                                    school.hire_teacher(main_db, course, teacher, __db_main)

                                else:
                                    print('\033[31;1m该讲师名已存在.\033[0m')

                            else:
                                print('\033[31;1m该课程名不存在.\033[0m')

                        elif if_cont == 'b':
                            break
                        else:
                            print('\033[31;1m输入错误，请重新输入.\033[0m')

                elif choice == '3':  # 创建班级
                    while True:
                        teacher_db = file_oper(__db_teacher, 'rb')
                        print('\033[33;1m目前学校【%s】已经存在的班级信息:\033[0m' % school_name)
                        res_course = information(main_db[school], 'None')[0]
                        if res_course:
                            for i in res_course:
                                k = res_course[i]
                                print('k:', k)
                                print(main_db[school][k])
                                print('--------------------------')
                                res_grade = information(main_db[school][k], 'grade')[1]
                                if not res_grade:
                                    print('\033[31;1m目前没有任何班级信息.\033[0m')
                        else:
                            print('\033[31;1m目前没有任何课程信息, 请先创建课程.\033[0m')

                        if_cont = input('\033[34;1m是否创建班级[y/b]:\033[0m').strip()
                        if if_cont == 'y':
                            grade_name = input('\033[34;1m输入班级名:\033[0m').strip()
                            course_name = input('\033[34;1m输入班级要上的课程:\033[0m').strip()
                            if course_name in res_course:
                                course = res_course[course_name]
                                if main_db[school][course]:
                                    teacher = main_db[school][course]['teacher']
                                    if grade_name not in res_grade:
                                        grade = Grade(grade_name, course_name, teacher.name)
                                        print('grade:', grade)
                                        school.create_grade(main_db, teacher_db, course, grade, teacher,
                                                            __db_main, __db_teacher)

                                else:
                                    print('\033[31;1m讲师不存在，请先招聘讲师.\033[0m')

                            else:
                                print('\033[31;1m课程名不存在，请重新输入.\033[0m')

                        elif if_cont == 'b':
                            break
                        else:
                            print('\033[31;1m输入错误，请重新输入.\033[0m')

                elif choice == '4':  # 返回
                    Flag = False
                else:
                    print('\033[31;1m输入错误，请重新输入.\033[0m')


def student_center():
    while True:
        choice = options(student_list)
        main_db = file_oper(__db_main, 'rb')
        teacher_db = file_oper(__db_teacher, 'rb')
        if choice == '1':
            student_name = input('\033[34;1m输入学生名:\033[0m').strip()
            res_school = information(main_db, 'main')[0]
            school_name = input('\033[34;1m输入学校名:\033[0m').strip()
            if school_name in res_school:
                school = res_school[school_name]
                res_course = information(main_db[school], 'course')[0]
                course_name = input('\033[34;1m输入课程名:\033[0m').strip()
                if course_name in res_course:
                    course = res_course[course_name]
                    if main_db[school][course].get('grade'):
                        for i in teacher_db:
                            i.course = course.name
                            teacher = i
                            grade = teacher_db[teacher].get('grade')
                            print('\033[33;1m课程【%s】的费用为【%s元】\033[0m' % (course_name, course.price))
                            if_pay = input('\033[34;1m是否支付当前费用(y支付):\033[0m').strip()
                            if if_pay == 'y':
                                grade.student.add(student_name)
                                grade.add_student(teacher_db, teacher, student_name, __db_teacher)
                                print('\033[32;1m选课成功！\033[0m')
                                any = input('输入任意键退出当前:')

                    else:
                        print('\033[31;1m讲师不存在，请先招聘讲师.\033[0m')
                else:
                    print('\033[31;1m课程不存在，请重新选择.\033[0m')
            else:
                print('\033[31;1m学校不存在，请重新选择.\033[0m')
        elif choice == '2':
            break
        else:
            print('\033[31;1m输入错误，请重新输入.\033[0m')


def teacher_center():
    teacher_db = file_oper(__db_teacher, 'rb')
    teacher_name = input('\033[34;1m输入讲师名:\033[0m').strip()
    res_teacher = information(teacher_db, 'None')[0]
    if res_teacher:
        if teacher_name in res_teacher:
            teacher = res_teacher[teacher_name]
            grade = teacher_db[teacher].get('grade')
            print('\033[33;1m欢迎进入讲师【%s】的管理中心\033[0m' % teacher_name)
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
            print('\033[31;1m讲师信息不存在，请重新输入.\033[0m')


def start():
    '''开始程序，根据选择的序号进入不同的视图'''
    while True:
        choice = options(main_list)
        if not choice: continue
        if choice == '1':
            print('\033[33;1m【学校中心】\033[0m')
            school_center()
        elif choice == '2':
            print('\033[33;1m【讲师中心】\033[0m')
            teacher_center()
        elif choice == '3':
            print('\033[33;1m【学生中心】\033[0m')
            student_center()
        elif choice == '4':
            print('退出')
            break


def file_oper(file, mode, *args):
    '''根据文件的读或者写，做不同的操作，读返回文件内容信息'''
    if mode == 'wb':
        data = args[0]
        with open(file, mode) as f:
            pickle.dump(data, f)
    elif mode == 'rb':
        with open(file, mode) as f:
            data = pickle.load(f)
            return data


def init_database():
    '''初始化学校信息'''
    sh = School('上海', '上海市')
    bj = School('北京', '北京市')
    if not os.path.exists(__db_main):
        data = {sh: {}, bj: {}}
        file_oper(__db_main, 'wb', data)
    if not os.path.exists(__db_teacher):
        data = {}
        file_oper(__db_teacher, 'wb', data)


if __name__ == '__main__':
    init_database()
    main_list = ['学校中心', '讲师中心', '学生中心', '退出']
    school_list = ['创建课程', '招聘讲师', '创建班级', '返回']
    student_list = ['学员注册', '返回']
    teacher_list = ['查看班级信息', '查看学员列表信息', '返回']
    start()
