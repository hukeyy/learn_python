#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, pickle

__main_db_file = 'main_dict'
__teacher_db_file = 'teacher_dict'


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
        print('\033[32;1m课程【%s】\t价格【%s元】\t周期【%s个月】\033[0m' % (
            self.name, self.price, self.time))


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
        print('\033[32;1m班级【%s】\t课程【%s】\t讲师【%s】\033[0m' % (
            self.name, self.course, self.teacher))

    def add_student(self, stduent_name, teacher_db, teacher, teacher_file):
        self.student.add(stduent_name)
        teacher_db[teacher] = {'grade': self}
        file_oper(teacher_file, 'wb', teacher_db)


def options(li):
    for i, k in enumerate(li):
        print(i + 1, k)
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
    if not os.path.exists(__main_db_file):
        sh = School('上海', '上海市')
        bj = School('北京', '北京市')
        data = {sh: {}, bj: {}}
        with open(__main_db_file, 'wb') as f:
            pickle.dump(data, f)
    if not os.path.exists(__teacher_db_file):
        data = {}
        with open(__teacher_db_file, 'wb') as f:
            pickle.dump(data, f)


def start():
    while True:
        choice = options(main_list)
        if choice == '1':
            school_center()
        elif choice == '2':
            teacher_center()
            pass
        elif choice == '3':
            student_center()
            pass
        elif choice == '4':
            break
        else:
            print('\033[31;1m输入错误，请重新输入.\033[0m')


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
        main_db = file_oper(__main_db_file, 'rb')
        res_school = information(main_db, 'main')[0]
        school_name = input('\033[34;1m输入要选择的学校名:\033[0m')
        if school_name in res_school:
            school_obj = res_school[school_name]
            while Flag:
                choice = options(school_list)
                if choice == '1':  # 创建课程
                    while True:
                        print('\n\033[32;1m目前【%s】学校已经有的课程信息:\033[0m' % school_name)
                        res_course = information(main_db[school_obj], 'course')[0]
                        if not res_course:
                            print('\033[31;1m目前没有课程信息.\033[0m')
                        if_cont = input('\033[34;1m是否要创建课程信息[y/b]:\033[0m')
                        if if_cont == 'y':
                            coures_name = input('\033[34;1m输入课程名:\033[0m')
                            if coures_name not in res_course:
                                coures_price = input('\033[34;1m输入课程价格:\033[0m')
                                coures_time = input('\033[34;1m输入课程周期:\033[0m')
                                course_obj = Course(coures_name, coures_price, coures_time)
                                school_obj.create_course(main_db, course_obj, __main_db_file)

                            else:
                                print('\033[31;1m该课程已信息.\033[0m')
                        else:
                            break


                elif choice == '2':  # 招聘讲师
                    while True:
                        print('\n\033[32;1m目前【%s】学校已经有的讲师信息:\033[0m' % school_name)
                        res_course = information(main_db[school_obj], 'None')[0]
                        if res_course:
                            for i in res_course:
                                k = res_course[i]
                                res_teacher = information(main_db[school_obj][k], 'teacher')[1]
                                if not res_teacher:
                                    print('\033[31;1m课程【%s】\t讲师【None】\033[0m' % k.name)
                        if_cont = input('\033[34;1m是否要招聘讲师[y/b]:\033[0m')
                        if if_cont == 'y':
                            name = input('\033[34;1m输入讲师名:\033[0m')
                            age = input('\033[34;1m输入讲师年龄:\033[0m')
                            course_name = input('\033[34;1m输入讲师要上的课程:\033[0m')
                            if course_name in res_course:
                                course_obj = res_course[course_name]
                                if name not in res_teacher:
                                    teacher_obj = Teacher(name, age, school_name, course_name)
                                    school_obj.hire_teacher(main_db, course_obj, teacher_obj,
                                                            __main_db_file)

                                else:
                                    print('\033[31;1m讲师信息已存在.\033[0m')

                            else:
                                print('\033[31;1m课程信息不存在，请先创建课程信息\033[0m')

                        else:
                            break

                elif choice == '3':  # 创建班级
                    while True:
                        teacher_db = file_oper(__teacher_db_file, 'rb')
                        print('\n\033[32;1m目前【%s】学校已经有的班级信息:\033[0m' % school_name)
                        res_course = information(main_db[school_obj], 'None')[0]
                        if res_course:
                            for i in res_course:
                                k = res_course[i]
                                res_grade = information(main_db[school_obj][k], 'grade')[1]
                                if not res_grade:
                                    print('\033[31;1m目前没有班级信息.\033[0m')

                        if_cont = input('\033[34;1m是否要创建班级[y/b]:\033[0m')
                        if if_cont == 'y':
                            grade_name = input('\033[34;1m输入班级名:\033[0m')
                            course_name = input('\033[34;1m输入班级要上的课程:\033[0m')
                            if course_name in res_course:
                                course_obj = res_course[course_name]
                                if main_db[school_obj][course_obj]:
                                    teacher_obj = main_db[school_obj][course_obj]['teacher']
                                    grade_obj = Grade(grade_name, course_name, teacher_obj.name)
                                    school_obj.create_grade(
                                        main_db, teacher_db, course_obj, teacher_obj, grade_obj,
                                        __main_db_file, __teacher_db_file
                                    )
                                else:
                                    print('\033[31;1m讲师信息不存在.\033[0m')

                            else:
                                print('\033[31;1m课程信息不存在.\033[0m')
                        else:
                            break




                elif choice == '4':
                    Flag = False
                else:
                    print('\033[31;1m输入错误，请重新输入.\033[0m')


def teacher_center():
    # main_db = file_oper(__main_db_file, 'rb')
    teacher_db = file_oper(__teacher_db_file, 'rb')
    res_teacher = information(teacher_db, 'None')[0]
    teacher_name = input('\033[34;1m输入讲师名:\033[0m').strip()
    if teacher_name in res_teacher:
        teacher_obj = res_teacher[teacher_name]
        grade_obj = teacher_db[teacher_obj]['grade']
        while True:
            print('\n\033[32;1m欢迎进入【%s】讲师的管理中心\033[0m' % teacher_name)
            choice = options(teacher_list)
            if choice == '1':
                print('\033[33;1m讲师【%s】的班级信息:' % teacher_name)
                print('\033[32;1m学校【%s】\t课程【%s】\t班级【%s】\033[0m' % (
                    teacher_obj.school, teacher_obj.course, grade_obj.name))
                any = input('\033[34;1m输入任意键退出当前:\033[0m')
            elif choice == '2':
                print('\033[33;1m讲师【%s】的学员列表信息:' % teacher_name)
                print('\033[32;1m班级【%s】\t学员列表【%s】\033[0m' % (
                    grade_obj.name, grade_obj.student))
                any = input('\033[34;1m输入任意键退出当前:\033[0m')
            elif choice == '3':
                break
            else:
                print('\033[31;1m输入错误，请重新输入.\033[0m')


def student_center():
    main_db = file_oper(__main_db_file, 'rb')
    teacher_db = file_oper(__teacher_db_file, 'rb')
    while True:
        choice = options(student_list)
        if choice == '1':
            student_name = input('\033[34;1m输入学生名:\033[0m').strip()
            res_school = information(main_db, 'main')[0]
            school_name = input('\033[34;1m输入学校名:\033[0m').strip()
            if school_name in res_school:
                school_obj = res_school[school_name]
                res_course = information(main_db[school_obj], 'course')[0]
                course_name = input('\033[34;1m输入课程名:\033[0m').strip()
                if course_name in res_course:
                    course_obj = res_course[course_name]
                    if main_db[school_obj][course_obj].get('grade'):
                        for i in teacher_db:
                            if course_obj.name == i.course:
                                teacher_obj = i
                                grade_obj = teacher_db[teacher_obj]['grade']
                        print('\033[32;1m课程【%s】的价格为【%s元】\033[0m' % (
                            course_obj.name, course_obj.price))
                        if_pay = input('\033[34;1m是否支付当前费用[y]:\033[0m').strip()
                        if if_pay == 'y':
                            # (self, stduent_name, teacher_db, teacher, teacher_file)
                            grade_obj.add_student(student_name, teacher_db, teacher_obj,
                                                  __teacher_db_file)
                            print('\033[32;1m选课成功.\033[0m')
                    else:
                        print('\033[31;1m讲师信息不存在，请先招聘讲师\033[0m')

                else:
                    print('\033[31;1m输入的课程不存在，请重新输入.\033[0m')

            else:
                print('\033[31;1m输入的学校名不存在，请重新输入.\033[0m')
        else:
            break


if __name__ == '__main__':
    init_database()
    main_list = ['学校中心', '讲师中心', '学生中心', '退出']
    school_list = ['创建课程', '招聘讲师', '创建班级', '返回']
    teacher_list = ['查看班级信息', '查看学员列表信息', '返回']
    student_list = ['学员注册', '返回']
    start()
