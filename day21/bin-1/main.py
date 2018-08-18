# -*- coding: utf-8 -*-
# Author: hkey
import os, pickle

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

__db_main = os.path.join(BASE_DIR, 'database', 'main_dict')
__db_teacher = os.path.join(BASE_DIR, 'database', 'teacher_dict')


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def cat_school(self):
        print('\033[32;1m学校名：【%s】\t地址：【%s】\033[0m' % (self.name, self.addr))

    def create_course(self, res_main, course, file):
        res_main[self][course] = {}
        file_oper(file, 'wb', res_main)

    def hire_teacher(self, res_main, course, teacher, file):
        res_main[self][course] = {'teacher': teacher}
        file_oper(file, 'wb', res_main)

    def create_grade(self, res_main, res_teacher, course, teacher, grade, file1, file2):
        res_main[self][course]['grade'] = grade
        file_oper(file1, 'wb', res_main)
        res_teacher[teacher] = {'grade': grade}
        file_oper(file2, 'wb', res_teacher)


class Course(object):
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time

    def cat_course(self):
        print('\033[32;1m课程：【%s】\t价格：【%s】\t周期：【%s个月】\033[0m' % (self.name, self.price, self.time))


class Teacher(object):
    def __init__(self, name, age, school, course, role='讲师'):
        self.name = name
        self.age = age
        self.school = school
        self.course = course
        self.role = role

    def cat_teacher(self):
        print('\033[32;1m课程：【%s】\t讲师：【%s】\033[0m' % (self.course, self.name))


class Grade(object):
    def __init__(self, name, course, teacher):
        student = set([])
        self.name = name
        self.course = course
        self.teacher = teacher
        self.student = student

    def cat_grade(self):
        print('\033[32;1m班级：【%s】\t课程：【%s】\t讲师：【%s】\033[0m' % (self.name, self.course, self.teacher))

    def add_student(self, student_name, res_teacher, teacher, file):
        self.student.add(student_name)
        res_teacher[teacher] = {'grade': self}
        file_oper(file, 'wb', res_teacher)


def file_oper(file, mode, *args):
    if mode == 'wb':
        with open(file, mode) as f:
            dict = args[0]
            pickle.dump(dict, f)
    elif mode == 'rb':
        with open(file, mode) as f:
            data = pickle.load(f)
            return data


def information(main_dict, mode, *args):
    if args:
        dict_info, set_info = {}, args[0]
    else:
        dict_info, set_info = {}, set([])

    if main_dict:
        for key in main_dict:
            if mode == 'main':
                key.cat_school()
            elif mode == 'course':
                key.cat_course()
            elif key == 'teacher' and mode == 'teacher':
                main_dict[key].cat_teacher()
                set_info.add(main_dict[key].name)
            elif key == 'grade' and mode == 'grade':
                main_dict[key].cat_grade()
                set_info.add(main_dict[key].name)

            if type(key) != str:
                dict_info[key.name] = key

    return dict_info, set_info


def student_center():
    print('\033[42;1m【学员中心】\033[0m')
    while True:
        choice = options(list_student)
        if choice == '1':
            print('\033[42;1m【学员注册】\033[0m')
            student_name = input('\033[34;1m输入学生名：\033[0m').strip()
            res_mian = file_oper(__db_main, 'rb')
            res_teacher = file_oper(__db_teacher, 'rb')
            school_dict = information(res_mian, 'main')[0]
            school_name = input('\033[34;1m输入学校名：\033[0m')
            if school_name in school_dict:
                school = school_dict[school_name]
                course_dict = information(res_mian[school], 'course')[0]
                course_name = input('\033[34;1m输入课程名：\033[0m').strip()
                if course_name in course_dict:
                    course = course_dict[course_name]
                    if res_mian[school][course].get('grade'):
                        for i in res_teacher:
                            if i.course == course.name:
                                teacher = i
                                grade = res_teacher[teacher]['grade']
                        print('\033[34;1m课程【%s】的费用【%s】\033[0m' %(course.name, course.price))
                        if_pay = input('是否支付【y】支付：').strip()
                        if if_pay == 'y':
                            # (self, student_name, res_teacher, teacher, file)
                            grade.add_student(student_name, res_teacher, teacher, __db_teacher)
                            print('\033[32;1m选课完成.\033[0m')
                            any = input('\033[32;1m输入任意键返回.\033[0m')
                        else:
                            break


                else:
                    print('\033[31;1m错误：课程信息不存在.\033[0m')

            else:
                print('\033[31;1m错误：学校信息不存在.\033[0m')

        elif choice == '2':
            break
        else:
            print('\033[31;1m错误：序号错误.\033[0m')


def teacher_center():
    print('\033[42;1m【讲师中心】\033[0m')
    res_teacher = file_oper(__db_teacher, 'rb')
    teacher_dict = information(res_teacher, 'teacher_center')[0]
    teacher_name = input('\033[34;1m输入讲师的姓名：\033[0m').strip()
    if teacher_name in teacher_dict:
        while True:
            teacher = teacher_dict[teacher_name]
            grade = res_teacher[teacher]['grade']
            choice = options(list_teacher)
            # ["查看班级", "查看班级学员列表", "返回"]
            if choice == '1':
                print('\033[32;1m讲师【%s】的班级信息'.center(40, '#') % teacher_name)
                print('\033[32;1m学校：【%s】\t班级：【%s】\t课程：【%s】' % (teacher.school, teacher.course, grade.name))
                any = input("\n\33[34;0m输入任意键退出当前\33[0m:")
            elif choice == '2':
                print('\033[32;1m讲师【%s】的班级学员信息'.center(40, '#') % teacher_name)
                print('\033[32;1m班级：【%s】\n学员：【%s】\033[0m' % (grade.name, grade.student))
                any = input("\n\33[34;0m输入任意键退出当前\33[0m:")

            elif choice == '3':
                break
            else:
                print('\033[31;1m错误：序号错误.\033[0m')


def school_center():
    print('\033[42;1m【学校中心】\033[0m')
    flag = True
    while flag:
        res_main = file_oper(__db_main, 'rb')
        res_teacher = file_oper(__db_teacher, 'rb')
        school_dict = information(res_main, 'main')[0]
        school_name = input('\033[34;1m选择学校：\033[0m')
        if school_name in school_dict:
            school = school_dict[school_name]
            while flag:
                print('\033[32;1m欢迎进入【%s】学校\033[0m'.center(50, '#') % school_name)
                choice = options(list_school)
                # ["创建班级", "招聘讲师", "创建课程", "返回"]
                if choice == '1':
                    print('\033[42;1m【创建班级】\033[0m')
                    while True:
                        print('\033[32;1m目前学校【%s】已有班级'.center(40, '#') % school_name)
                        course_dict = information(res_main[school], 'None')[0]
                        set_info = set([])
                        for i in course_dict:
                            k = course_dict[i]
                            grade_dict = information(res_main[school][k], 'grade', set_info)[1]

                        if_cont = input('\033[34;1m是否创建班级【y】创建【b】退出:\033[0m').strip()
                        if if_cont == 'y':
                            grade_name = input('\033[34;1m输入班级名：\033[0m').strip()
                            course_name = input('\033[34;1m输入班级要上的课程：\033[0m').strip()
                            if course_name in course_dict:
                                course = course_dict[course_name]
                                if res_main[school][course]:
                                    teacher = res_main[school][course]['teacher']
                                    grade = Grade(grade_name, course_name, teacher.name)
                                    # (self, res_main, res_teacher, course, teacher, grade, file1, file2)
                                    school.create_grade(res_main, res_teacher, course, teacher, grade, __db_main,
                                                        __db_teacher)

                                else:
                                    print('\033[31;1m错误：讲师信息不存在')
                            else:
                                print('\033[31;1m错误：课程信息不存在.\033[0m')
                        elif if_cont == 'b':
                            break

                elif choice == '2':
                    print('\033[42;1m【招聘讲师】\033[0m')
                    while True:
                        print('\033[32;1m目前学校【%s】已有课程及讲师'.center(40, '#') % school_name)
                        course_dict = information(res_main[school], 'None')[0]
                        set_info = set([])
                        for i in course_dict:
                            k = course_dict[i]
                            teacher_dict = information(res_main[school][k], 'teacher', set_info)[1]
                            if not teacher_dict:
                                print('\033[31;1m课程：【%s】\t讲师：【None】\033[0m' % i)
                        if_cont = input('\033[34;1m是否招聘讲师【y】招聘【b】退出:\033[0m').strip()
                        if if_cont == 'y':
                            teacher_name = input('\033[34;1m输入讲师的名字：\033[0m').strip()
                            teacher_age = input('\033[34;1m输入讲师的年龄：\033[0m').strip()
                            course_name = input('\033[34;1m输入讲师的课程：\033[0m').strip()
                            if course_name in course_dict:
                                course = course_dict[course_name]
                                if teacher_name not in teacher_dict:
                                    teacher = Teacher(teacher_name, teacher_age, school_name, course_name)
                                    # (self, res_main, course, teacher, file)
                                    school.hire_teacher(res_main, course, teacher, __db_main)

                                else:
                                    print('\033[31;1m错误：讲师信息已存在.\033[0m')
                            else:
                                print('\033[31;1m课程信息不存在，请先创建课程.\033[0m')


                        elif if_cont == 'b':
                            break


                elif choice == '3':
                    print('\033[42;1m【创建课程】\033[0m')
                    while True:
                        print('\033[32;1m目前学校【%s】已有课程'.center(40, '#') % school_name)
                        course_dict = information(res_main[school], 'course')[0]
                        if_cont = input('\033[34;1m是否要创建课程【y】创建【b】退出:\033[0m').strip()
                        if if_cont == 'y':
                            course_name = input('\033[34;1m输入课程名：\033[0m').strip()
                            if course_name not in course_dict:
                                course_price = input('\033[34;1m课程【%s】的价格：\033[0m' % course_name).strip()
                                course_time = input('\033[34;1m课程【%s】的周期：\033[0m' % course_name).strip()
                                course = Course(course_name, course_price, course_time)
                                school.create_course(res_main, course, __db_main)

                            else:
                                print('\033[31;1m错误：课程信息已存在.\033[0m')
                        elif if_cont == 'b':
                            break


                elif choice == '4':
                    flag = False
                else:
                    print('\033[31;1m错误：序号错误。\033[0m')

        else:
            print('\033[31;1m错误：输入的学校不存在.\033[0m')


def init_database():
    sh = School('上海', '上海市')
    bj = School('北京', '北京市')
    if not os.path.exists(__db_main):
        with open(__db_main, 'wb') as f:
            dict = {sh: {}, bj: {}}
            pickle.dump(dict, f)
    if not os.path.exists(__db_teacher):
        with open(__db_teacher, 'wb') as f:
            dict = {}
            pickle.dump(dict, f)


def options(list):
    for k, v in enumerate(list, 1):
        print(k, v)
    choice = input('\033[34;1m请选择模式：\033[0m').strip()
    return choice


def start():
    while True:
        choice = options(list_main)
        # ["学生中心", "讲师中心", "学校中心", "退出"]
        if choice == '1':
            student_center()
        elif choice == '2':
            teacher_center()
        elif choice == '3':
            school_center()
        elif choice == '4':
            break
        else:
            print('\033[31;1m错误：序号错误.\033[0m')


if __name__ == '__main__':
    init_database()
    list_main = ["学生中心", "讲师中心", "学校中心", "退出"]
    list_school = ["创建班级", "招聘讲师", "创建课程", "返回"]
    list_teacher = ["查看班级", "查看班级学员列表", "返回"]
    list_student = ["学员注册", "返回"]
    start()
