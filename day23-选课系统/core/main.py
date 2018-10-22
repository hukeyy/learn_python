#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import pickle, os
from conf import settings
from model import school


def file_oper(file, mode, *args):
    if mode == 'wb':
        data = args[0]
        with open(file, mode) as f:
            pickle.dump(data, f)
    elif mode == 'rb':
        with open(file, mode) as f:
            data = pickle.load(f)
            return data


def manage_school():
    print('\033[33;1m[manage_school]\033[0m')
    file_data = file_oper(settings.school_db_file, 'rb')
    school_dict = {}
    while True:
        for k in file_data.keys():
            k.cat_school()
            school_dict[k.name] = k
        school_name = input('\033[34;1m请输入学校名：\033[0m').strip()
        if not school_name: continue
        if school_name in school_dict:
            school = school_dict[school_name]
            print('\033[32;1m欢迎进入【%s】学院\033[0m'.center(50,'-') % school.name)
            choice = options(list_school)
            print(choice)




            break



def manage_teacher():
    print('\033[33;1m[manage_teacher]\033[0m')


def manage_student():
    print('\033[33;1m[manage_student]\033[0m')


def init_database():
    bj = school.School('北京', '北京市')
    sh = school.School('上海', '上海市')
    if not os.path.exists(settings.school_db_file):
        dic = {bj:{}, sh:{}}
        file_oper(settings.school_db_file, 'wb', dic)


def options(li):
    for i, v in enumerate(li):
        print(i+1, v)
    choice = input('>>>').strip()
    return choice


def start():
    init_database()
    while True:
        choice = options(list_main)
        if choice == '1':
            manage_school()
        elif choice == '2':
            manage_teacher()
        elif choice == '3':
            manage_student()
        elif choice == '4':
            break
        else:
            print('\033[31;1m错误：输入错误，请重新输入.\033[0m')


if __name__ == '__main__':
    list_main = ['学校中心', '讲师中心', '学员中心', '退出']
    list_school = ['创建课程', '创建班级', '招聘讲师', '返回']