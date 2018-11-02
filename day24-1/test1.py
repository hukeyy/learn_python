#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
__main_db = os.path.join(BASE_DIR, 'school_dict')
__teacher_db = os.path.join(BASE_DIR, 'teacher_dict')


class School:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def cat_school(self):
        print('\033[32;1m学校名【%s】\t地址【%s】\033[0m' % (self.name, self.addr))

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


class Course:
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time

    def cat_course(self):
        print('\033[32;1m课程名【%s】\t价格【%s元】\t周期【%s个月】\033[0m' % (self.name, self.price, self.time))


class Teacher:
    def __init__(self, name, school, course):
        self.name = name
        self.school = school
        self.course = course

    def cat_teacher(self):
        print('\033[32;1m课程名【%s】\t讲师名【%s】\033[0m' % (self.course, self.name))


class Grade:
    def __init__(self, name, course, teacher):
        self.name = name
        self.course = course
        self.teacher = teacher
        self.student = set([])

    def cat_grade(self):
        print('\033[32;1m班级名【%s】\t讲师名【%s】\033[0m' % (self.course, self.name))

    def add_student(self, teacher_db, teacher, teacher_file):
        teacher_db[teacher] = {'grade': self}
        file_oper(teacher_file, 'wb', teacher_db)


def options(li):
    for k, i in enumerate(li):
        print(k+1, i)
    choice = input('>>>').strip()
    return choice


def file_oper(file, mode, *args):
    if mode == 'wb':
        with open(file, mode) as f:
            data = args[0]
            pickle.dump(data, f)
    elif mode == 'rb':
        with open(file, mode) as f:
            data = pickle.load(f)
            return data


def init_database():
    sh = School('上海', '上海市')
    bj = School('北京', '北京市')
    if not os.path.exists(__main_db):
        data = {sh:{}, bj:{}}
        file_oper(__main_db, 'wb', data)
    if not os.path.exists(__teacher_db):
        data = {}
        file_oper(__teacher_db, 'wb', data)


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
    Flag = True
    while Flag:
        main_db = file_oper(__main_db, 'rb')
        res_school = information(main_db, 'main')[0]
        school_name = input('\033[34;1m选择学校：\033[0m')
        if school_name in res_school:
            school = res_school[school_name]
            while Flag:
                choice = options(school_list)
                if choice == '1':   # 创建课程
                    while True:
                        print('\033[33;1m目前【%s】学校已经存在的课程:\033[0m' % school_name)
                        res_course = information(main_db[school], 'course')[0]
                        if not res_course:
                            print('\033[31;1m目前没有课程.\033[0m')
                        if_cont = input('\033[34;1m是否要创建课程[y/b]：\033[0m')
                        if if_cont == 'y':
                            course_name = input('\033[34;1m输入课程名：\033[0m')
                            if course_name not in res_course:
                                course_price = input('\033[34;1m输入课程名价格：\033[0m')
                                course_time = input('\033[34;1m输入课程名周期：\033[0m')
                                course = Course(course_name, course_price, course_time)
                                school.create_course(main_db, course, __main_db)

                            else:
                                print('\033[31;1m课程信息已存在.\033[0m')
                        elif if_cont == 'b':
                            break
                elif choice == '2': # 招聘讲师
                    while True:
                        print('\033[33;1m目前【%s】学校已经存在的讲师:\033[0m' % school_name)
                        res_course = information(main_db[school], 'None')[0]
                        if res_course:
                            for i in res_course:
                                k = res_course[i]
                                res_teacher = information(main_db[school][k], 'teacher')[1]
                                if not res_teacher:
                                    print('\033[31;1m课程名【%s】\t讲师名【None】\033[0m' % k.name)
                        if_cont = input('\033[34;1m是否要招聘讲师[y/b]：\033[0m')
                        if if_cont == 'y':
                            teacher_name = input('\033[34;1m输入讲师名：\033[0m')
                            course_name = input('\033[34;1m输入讲师要教授的课程名：\033[0m')
                            if course_name in res_course:
                                course = res_course[course_name]
                                if teacher_name not in res_teacher:
                                    teacher = Teacher(teacher_name, school_name, course_name)
                                    school.hire_teacher(main_db, course, teacher, __main_db)
                            else:
                                print('\033[31;1m课程信息不存在.\033[0m')

                        elif if_cont == 'b':
                            break
                elif choice == '3': # 创建班级
                    while True:
                        teacher_db = file_oper(__teacher_db, 'rb')
                        print('\033[33;1m目前【%s】学校已经存在的班级信息:\033[0m' % school_name)
                        res_course = information(main_db[school], 'None')[0]
                        if res_course:
                            for i in res_course:
                                k = res_course[i]
                                res_grade = information(main_db[school][k], 'grade')[1]
                                if not res_grade:
                                    print('\033[31;1m目前班级信息不存在.\033[0m')
                        if_cont = input('\033[34;1m是否要创建班级[y/b]：\033[0m')
                        if if_cont == 'y':
                            grade_name = input('\033[34;1m输入班级名：\033[0m')
                            course_name = input('\033[34;1m输入班级要上的课程名：\033[0m')
                            if course_name in res_course:
                                course = res_course[course_name]
                                if main_db[school][course]:
                                    teacher = main_db[school][course]['teacher']
                                    if grade_name not in res_grade:
                                        grade = Grade(grade_name, course_name, teacher.name)
                                        school.create_grade(main_db, teacher_db, course, teacher, grade,
                                                            __main_db, __teacher_db)

                                    else:
                                        print('\033[31;1m班级信息已存在.\033[0m')


                            else:
                                print('\033[31;1m课程信息不存在.\033[0m')

                        elif if_cont == 'b':
                            break

                elif choice == '4':
                    Flag = False
                else:
                    print('\033[31;1m输入错误，请重新输入。\033[0m')


def teacher_center():
    teacher_db = file_oper(__teacher_db, 'rb')
    teacher_name = input('\033[34;1m请输入讲师姓名：\033[0m')
    res_teacher = information(teacher_db, 'None')[0]
    if teacher_name in res_teacher:
        print('\033[32;1m欢迎进入讲师【%s】的管理中心\033[0m' % teacher_name)
        teacher = res_teacher[teacher_name]
        if teacher_db[teacher]:
            grade = teacher_db[teacher]['grade']
            while True:
                choice = options(teacher_list)
                if choice == '1':
                    print('\033[32;1m学校【%s】\t班级【%s】\033[0m' % (teacher.school, grade.name))
                    any = input('\033[34;1m输入任意键退出当前:\033[0m')
                elif choice == '2':
                    print('\033[32;1m班级【%s】\t学员【%s】\033[0m' % (grade.name, grade.student))
                    any = input('\033[34;1m输入任意键退出当前:\033[0m')
                elif choice == '3':
                    break


def student_center():
    main_db = file_oper(__main_db, 'rb')
    teacher_db = file_oper(__teacher_db, 'rb')
    while True:
        choice = options(student_list)
        if choice == '1':   # 学员注册
            student_name = input('\033[34;1m输入学生名：\033[0m')
            res_school = information(main_db, 'main')[0]
            school_name = input('\033[34;1m选择学校名：\033[0m')
            if school_name in res_school:
                school = res_school[school_name]
                res_course = information(main_db[school], 'course')[0]
                course_name = input('\033[34;1m选择课程名：\033[0m')
                if course_name in res_course:
                    course = res_course[course_name]
                    if main_db[school][course].get('grade'):
                        for i in teacher_db:
                            if i.course == course.name:
                                teacher = i
                                grade = teacher_db[teacher]['grade']
                        print('\033[32;1m课程【%s】的价格【%s】\033[0m' % (course.name, course.price))
                        if_pay = input('\033[34;1m是否支付当前费用[y]:\033[0m')
                        if if_pay == 'y':
                            grade.student.add(student_name)
                            grade.add_student(teacher_db, teacher, __teacher_db)
                            print('\033[32;1m选课成功.\033[0m')
                            any = input('\033[34;1m输入任意键退出当前:\033[0m')

                    else:
                        print('\033[31;1m讲师信息不存在，请重新输入。\033[0m')

                else:
                    print('\033[31;1m课程不存在，请重新输入。\033[0m')
            else:
                print('\033[31;1m学校不存在，请重新输入。\033[0m')

        elif choice == '2':
            break


def start():
    while True:
        choice = options(main_list)
        if choice == '1':
            school_center()
        elif choice == '2':
            teacher_center()
        elif choice == '3':
            student_center()
        elif choice == '4':
            break
        else:
            print('\033[31;1m输入错误，请重新输入。\033[0m')


if __name__ == '__main__':
    init_database()
    main_list = ['学校中心', '讲师中心', '学生中心', '退出']
    school_list = ['创建课程', '招聘讲师', '创建班级', '返回']
    teacher_list = ['查看班级信息', '查看学员列表信息', '返回']
    student_list = ['学员注册', '返回']
    start()


