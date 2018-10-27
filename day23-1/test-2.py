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


def options(li):
    '''序号和标题循环打印，返回选择序号'''
    for i, k in enumerate(li):
        print(i + 1, k)
    choice = input('>>>').strip()
    return choice


def information(db, mode):
    dict_info = {}
    if db:
        for key in db:
            if mode == 'main':
                key.cat_school()
            if not isinstance(key, str):
                dict_info[key.name] = key

        return dict_info


def school_center():
    Flag = True
    while Flag:
        main_db = file_oper(__db_main, 'rb')
        res_school = information(main_db, 'main')
        school_name = input('\033[34;1m选择学校名:\033[0m')


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
        elif choice == '3':
            print('\033[33;1m【学生中心】\033[0m')
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
    start()
