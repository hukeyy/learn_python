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


class Course(object):
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time

    def cat_course(self):
        print('\033[32;1m课程【%s】\t价格【%s元】\t周期【%s个月】\033[0m' % (self.name, self.price, self.time))


def options(li):
    for i, k in enumerate(li):
        print(i+1, k)
    choice = input('>>>').strip()
    return choice


def file_oper(file, mode, *args):
    if mode == 'wb':
        with open(file, mode) as f:
            data = args[0]
            pickle.dump(f, data)
    elif mode == 'rb':
        with open(file, mode) as f:
            data = pickle.load(f)
            return data


def init_database():
    if not os.path.exists(__main_db_file):
        sh = School('上海', '上海市')
        bj = School('北京', '北京市')
        data = {sh:{}, bj:{}}
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
        elif choice == '3':
            student_center()
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







if __name__ == '__main__':
    init_database()
    main_list = ['学校中心', '讲师中心', '学生中心', '退出']
    school_list = ['创建课程', '招聘讲师', '创建班级', '返回']
    start()



























