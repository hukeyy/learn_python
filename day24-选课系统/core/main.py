#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

from conf import settings


# db_path = os.path.join(BASE_DIR, 'database')
# main_list = ['学校中心', '讲师中心', '学生中心', '退出']
# school_list = ['创建课程', '招聘讲师', '创建班级', '退出']

def options(list):
    for v, k in enumerate(list, 1):
        print(v, k)

    choice = input('\033[34;1m请选择模式：\033[0m').strip()
    return choice



def school_center():
    print('\033[35;1m学校中心\033[0m')
    flag = True
    while flag:
        print('\033[32;1m欢迎进入学校中心\033[0m'.center(50, '#'))
        choice = options(settings.school_list)


def teacher_center():
    print('\033[35;1m讲师中心\033[0m')


def student_center():
    print('\033[35;1m学生中心\033[0m')


def main():
    while True:
        choice = options(settings.main_list)
        if not choice: continue
        if choice == '1':
            school_center()
        elif choice == '2':
            teacher_center()
        elif choice == '3':
            student_center()
        elif choice == '4':
            break
        else:
            print('\033[31;1m错误：序号错误.\033[0m')
