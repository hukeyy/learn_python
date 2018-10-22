#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import pickle, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 数据库地址
database_file = os.path.join(BASE_DIR, 'school')

class School(object):
    '''学校类'''
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
    def cat_school(self):
        print('\033[32;1m学校名：【%s】，地址：【%s】.\033[0m' %(self.name, self.addr))

    def create_course(self, dic, course, file):
        dic[self][course] = {}
        file_oper(file, 'wb', dic)


    def create_grade(self, grade):
        self.grade = grade


class Course(object):
    '''课程类'''
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time
    def cat_course(self):
        print('\033[32;1m课程：【%s】\t价格：【%s元】\t周期【%s个月】\033[0m' % (self.name, self.price, self.time))


class Grade(object):
    '''班级类'''
    def __init__(self, name, course, teacher):
        self.name = name
        self.course = course
        self.teacher = teacher


def file_oper(file, mode, *args):
    if mode == 'wb':
        data = args[0]
        with open(file, mode) as f:
            pickle.dump(data, f)
    elif mode == 'rb':
        with open(file, mode) as f:
            data = pickle.load(f)
            return data


def options(li):
    for i, v in enumerate(li):
        print(i+1, v)
    choice = input('>>>').strip()
    return choice


def init_database():
    sh = School('上海', '上海市')
    bj = School('北京', '北京市')
    if not os.path.exists(database_file):
        school_dict = {sh:{}, bj:{}}
        file_oper(database_file, 'wb', school_dict)


def information(dic, mode, *args):
    if args:
        dict_info, set_info = {}, args[0]
    else:
        dict_info, set_info = {}, set([])
    if dic:
        for key in dic:
            if mode == 'course':
                key.cat_course()
            elif mode == 'main':
                key.cat_school()
            if not isinstance(key, str):
                dict_info[key.name] = key
    print(dict_info)
    return dict_info, set_info


def school_center():
    Flag = True
    while Flag:
        file_db = file_oper(database_file, 'rb')
        res_main = information(file_db, 'main')[0]
        school_name = input('\033[34;1m请输入学校名：\033[0m').strip()
        if school_name in res_main:
            school = res_main[school_name]
            while Flag:
                print('\033[32;1m欢迎进入【%s】学校\033[0m'.center(50, '#') % school_name)
                choice = options(school_list)
                if choice == '1':   # 创建课程
                    pass

                elif choice == '2': # 创建班级
                    pass
                elif choice == '3': # 招聘讲师
                    pass
                elif choice == '4':
                    Flag = False
                else:
                    print('\033[31;1m错误：输入错误，请重新输入.\033[0m')
                    continue



        break






def teacher_center():
    print('\033[33;1m[teacher_center]\033[0m')


def student_center():
    print('\033[33;1m[student_center]\033[0m')


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
            print('\033[31;1m错误：输入错误，请重新输入.\033[0m')


if __name__ == '__main__':
    main_list = ['学校中心', '讲师中心', '学生中心', '退出']
    school_list = ['创建课程', '创建班级', '招聘讲师', '返回']
    init_database()
    start()


