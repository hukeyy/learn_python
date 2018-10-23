#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

__db_school_file = os.path.join(BASE_DIR, 'school_dict')
__db_teacher_file = os.path.join(BASE_DIR, 'teacher_dict')


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def cat_school(self):
        print('\033[32;1m学校名：【%s】\t地址：【%s】.\033[0m' %(self.name, self.addr))

    def create_course(self, db, course, main_file):
        db[self][course] = {}
        file_oper(main_file, 'wb', db)

    def hire_teacher(self, db, course, teacher, main_file):
        db[self][course] = {'teacher': teacher}
        file_oper(main_file, 'wb', db)



class Course(object):
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time

    def cat_course(self):
        print('\033[32;1m课程：【%s】\t价格：【%s元】\t周期：【%s个月】\033[0m' %(self.name, self.price, self.time))


class Grade(object):
    def __init__(self, name, course, teacher):
        student = set([])
        self.name = name
        self.course = course
        self.teacher = teacher
        self.student = student

    def cat_grade(self):
        print('\033[32;1m班级名：【%s】\t课程：【%s】\t讲师：【%s】\033[0m' %(self.name, self.course, self.teacher))


class Teacher(object):
    def __init__(self, name, age, school, course, role='讲师'):
        self.name = name
        self.age = age
        self.school = school
        self.course = course
        self.role = role

    def cat_teacher(self):
        print('\033[32;1m课程：【%s】\t讲师：【%s】\033[0m' % (self.course, self.name))





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
    if not os.path.exists(__db_school_file):
        data = {sh: {}, bj: {}}
        file_oper(__db_school_file, 'wb', data)

    if not os.path.exists(__db_teacher_file):
        data = {}
        file_oper(__db_teacher_file, 'wb', data)

def options(li):
    for i, k in enumerate(li):
        print(i+1, k)
    choice = input('>>>').strip()
    return choice

def information(db, mode, *args):
    if args:
        dict_info, set_info = {}, args[0]
    else:
        dict_info, set_info = {}, args

    if db:
        for key in db:
            if mode == 'main':
                key.cat_school()
            elif mode == 'course':
                key.cat_course()
            elif mode == 'teacher' and key == 'teacher':
                db[key].cat_teacher()
                set_info.add(db[key].name)
            if not isinstance(key, str):
                dict_info[key.name] = key

    return dict_info, set_info




def school_center():
    print('\033[35;1m[school_center]\033[0m')
    Flag = True
    while Flag:
        main_db = file_oper(__db_school_file, 'rb')
        res_shool = information(main_db, 'main')[0]
        school_name = input('\033[34;1m输入学校名：\033[0m').strip()
        if school_name in res_shool:
            school = res_shool[school_name]
            while Flag:
                choice = options(school_list)
                if not choice: continue
                if choice == '1':   # 创建课程
                    print('\033[33;1m目前【%s】学校已有课程信息：\033[0m' % school.name)
                    res_course = information(main_db[school], 'course')[0]
                    if not res_course:
                        print('\033[31;1m没有课程.\n\033[0m')
                    if_cont = input('\033[34;1m是否创建课程(y/b):\033[0m').strip()
                    if if_cont == 'y':
                        course_name = input('\033[34;1m输入课程名：\033[0m').strip()
                        if course_name not in res_course:
                            course_price = input('\033[34;1m输入课程价格：\033[0m').strip()
                            course_time = input('\033[34;1m输入课程周期：\033[0m').strip()
                            course = Course(course_name, course_price, course_time)
                            school.create_course(main_db, course, __db_school_file)
                        else:
                            print('\033[31;1m错误：【%s】课程已存在.\033[0m' % course_name)
                    elif if_cont == 'b':
                        print('返回')

                    else:
                        print('\033[31;1m输入错误.\033[0m')

                elif choice == '2': # 招聘讲师
                    while True:
                        res_course = information(main_db[school], 'None')[0]
                        if res_course:
                            for i in res_course:
                                k = res_course[i]
                                res_teacher = information(main_db[school][k], 'teacher')[1]
                                if not res_teacher:
                                    print('\033[31;1m课程：【%s】\t讲师：【None】\033[0m' % course.name)


                elif choice == '3': # 创建班级
                    while True:
                        res_course = information(main_db, 'None')[0]

                elif choice == '4': # 返回
                    Flag = False
                else:
                    print('\033[31;1m错误：输入错误，请重新输入.\033[0m')





        Flag = False


def teacher_center():
    print('\033[35;1m[teacher_center]\033[0m')



def student_center():
    print('\033[35;1m[student_center]\033[0m')



def start():
    while True:
        choice = options(main_list)
        if not choice: continue
        if choice == '1':   # 学校中心
            school_center()
        elif choice == '2': # 讲师中心
            teacher_center()
        elif choice == '3': # 学生中心
            student_center()
        elif choice == '4':
            break
        else:
            print('\033[31;1m错误：输入错误，请重新输入.\033[0m')


if __name__ == '__main__':
    main_list = ['学校中心', '讲师中心', '学生中心', '退出']
    school_list = ['创建课程', '招聘讲师', '创建班级', '返回']
    init_database()
    start()














