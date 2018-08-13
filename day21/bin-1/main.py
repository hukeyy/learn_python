# -*- coding: utf-8 -*-
# Author: hkey
import os, pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

__db_main = os.path.join(BASE_DIR, 'database', 'main_dict')
__db_teacher = os.path.join(BASE_DIR, 'database', 'teacher_dict')

class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def cat_school(self):
        print('\033[32;1m学校名：【%s】\t地址：【%s】\033[0m' % (self.name, self.addr))

    def create_course(self, main_dict, course, file):
        main_dict[self][course] = {}
        file_oper(file, 'wb', main_dict)

    def hire_teacher(self, main_dict, course, teacher, file):
        main_dict[self][course]= {'teacher': teacher}
        file_oper(file, 'wb', main_dict)
    def create_grade(self, main_dict, teacher_dict, course, teacher, grade, file1, file2):
        main_dict[self][course]['grade'] = grade
        file_oper(file1, 'wb', main_dict)
        teacher_dict[teacher] = {'grade': grade}
        file_oper(file2, 'wb', teacher_dict)


class Course(object):
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time

    def cat_course(self):
        print('\033[32;1m课程名：【%s】\t价格：【%s】\t周期：【%s个月】\033[0m' %(self.name, self.price, self.time))

class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(People):
    def __init__(self, name, age, school, course, role='讲师'):
        super(Teacher, self).__init__(name, age)
        self.school = school
        self.course = course
        self.role = role

    def cat_teacher(self):
        print('\033[32;1m课程：【%s】\t讲师：【%s】\033[0m' % (self.course, self.name))

class Grade(object):
    def __init__(self, name, school, course, teacher):
        student = set([])
        self.name = name
        self.school = school
        self.course = course
        self.teacher = teacher

    def cat_grade(self):
        print('\033[32;1m班级：【%s】\t课程：【%s】讲师：【%s】\033[0m' %(self.name, self.course, self.teacher))


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
            elif mode == 'teacher' and key == 'teacher':
                main_dict[key].cat_teacher()
                set_info.add(main_dict[key].name)
            elif mode == 'grade' and key == 'grade':
                main_dict[key].cat_grade()
                set_info.add(main_dict[key].name)
            if type(key) != str:
                dict_info[key.name] = key

    return dict_info, set_info

def student_center():
    print('\033[42;1m【学生中心】\033[0m')

def teacher_center():
    print('\033[42;1m【教师中心】\033[0m')

def school_center():
    print('\033[42;1m【学校中心】\033[0m')
    flag = True
    while flag:
        res_main = file_oper(__db_main, 'rb')
        school_dict = information(res_main, 'main')[0]
        school_name = input('\033[34;1m输入要选择的学校名：\033[0m').strip()
        if school_name in school_dict:
            school = school_dict[school_name]
            print('\033[32;1m欢迎来到【%s】学校\033[0m' % school_name)
            while flag:
                choice = options(list_school)
                # ["创建班级", "招聘讲师", "创建课程", "返回"]
                if choice == '1':
                    print('\033[32;1m【创建班级】\033[0m')
                    while True:
                        print('\033[32;1m学校【%s】目前已有班级\033[0m'.center(50, '#') % school_name)
                        teacher_dict = file_oper(__db_teacher, 'rb')
                        course_dict = information(res_main[school], 'None')[0]
                        set_info = set([])
                        for i in course_dict:
                            k = course_dict[i]
                            grade_dict = information(res_main[school][k], 'grade', set_info)[1]
                        if_cont = input('\033[32;1m是否创建班级【y】创建【b】退出.\033[0m').strip()
                        if if_cont == 'y':
                            grade_name = input('\033[34;1m输入班级名：\033[0m').strip()
                            course_name = input('\033[34;1m输入班级要上的课程：\033[0m').strip()
                            if course_name in course_dict:
                                course = course_dict[course_name]
                                if res_main[school][course]:
                                    teacher = res_main[school][course]['teacher']
                                    if grade_name not in grade_dict:
                                        grade = Grade(grade_name, school_name, course_name, teacher.name)
                                        # (self, main_dict, teacher_dict, course, teacher, grade, file1, file2)
                                        school.create_grade(res_main, teacher_dict, course, teacher, grade,
                                                            __db_main, __db_teacher)

                                    else:
                                        print('\033[31;1m错误：班级信息已存在.\033[0m')

                                else:
                                    print('\033[31;1m错误：老师信息不存在.\033[0m')



                            else:
                                print('\033[31;1m错误：课程还未创建.\033[0m')

                        elif if_cont == 'b':
                            break



                elif choice == '2':
                    print('\033[32;1m【招聘讲师】\033[0m')
                    while True:
                        print('\033[32;1m学校【%s】目前已有课程及讲师\033[0m'.center(50, '#') % school_name)
                        course_dict = information(res_main[school], 'None')[0]
                        set_info = set([])
                        for i in course_dict:
                            k = course_dict[i]
                            teacher_dict = information(res_main[school][k], 'teacher')[1]
                            if not teacher_dict:
                                print('\033[31;1m课程：【%s】\t讲师：【None】\033[0m' % i)

                        if_cont = input('\033[34;1m是否招聘讲师【y】招聘【b】退出.\033[0m').strip()
                        if if_cont == 'y':
                            teacher_name = input('\033[34;1m输入老师的名字：\033[0m').strip()
                            teacher_age = input('\033[34;1m输入老师的年龄：\033[0m').strip()
                            course_name = input('\033[34;1m输入老师教授的课程：\033[0m').strip()
                            if course_name in course_dict:
                                course = course_dict[course_name]
                                teacher = Teacher(teacher_name, teacher_age, school_name, course_name)
                                school.hire_teacher(res_main, course, teacher, __db_main)

                            else:
                                print('\033[31;1m错误：课程不存在，请先创建课程.\033[0m')



                        elif if_cont == 'b':
                            break


                elif choice == '3':
                    print('\033[32;1m【创建课程】\033[0m')
                    while True:
                        print('\033[32;1m学校【%s】目前已有课程\033[0m'.center(50, '#') % school_name)
                        course_dict = information(res_main[school], 'course')[0]
                        if_cont = input('\033[32;1m是否创建课程【y】创建【b】退出\033[0m').strip()
                        if if_cont == 'y':
                            course_name = input('\033[34;1m输入课程名：\033[0m').strip()
                            if course_name not in course_dict:
                                course_price = input('\033[34;1m输入课程【%s】的价格：\033[0m' % course_name).strip()
                                course_time = input('\033[34;1m输入课程【%s】的周期：\033[0m' % course_name).strip()
                                course = Course(course_name, course_price, course_time)
                                school.create_course(res_main, course, __db_main)

                            else:
                                print('\033[31;1m错误：课程已存在.\033[0m')
                        elif if_cont == 'b':
                            break
                        else:
                            print('\033[31;1m错误：序号错误，请重新输入.\033[0m')



                elif choice == '4':
                    flag = False
                else:
                    print('\033[31;1m错误：序号错误，请重新输入.\033[0m')

        else:
            print('\033[31;1m错误：学校名不存在，请重新输入.\033[0m')





def options(list):
    for k, v in enumerate(list, 1):
        print(k, v)
    choice = input('\033[34;1m请选择模式：\033[0m')
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
            print('\033[31;1m错误：序号错误，请重新输入.\033[0m')





def init_database():
    bj = School('北京', '北京市')
    sh = School('上海', '上海市')
    if not os.path.exists(__db_main):
        with open(__db_main, 'wb') as f:
            dict = {bj:{}, sh:{}}
            pickle.dump(dict, f)
    if not os.path.exists(__db_teacher):
        with open(__db_teacher, 'wb') as f:
            dict = {}
            pickle.dump(dict, f)


if __name__ == '__main__':
    init_database()
    list_main = ["学生中心", "讲师中心", "学校中心", "退出"]
    list_school = ["创建班级", "招聘讲师", "创建课程", "返回"]
    list_teacher = ["查看班级", "查看班级学员列表", "返回"]
    list_student = ["学员注册", "返回"]
    start()
