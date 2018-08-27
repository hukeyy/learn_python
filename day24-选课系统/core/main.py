#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import pickle, os
from conf import settings
from core import file_oper

# db_path = os.path.join(BASE_DIR, 'database')
# main_list = ['学校中心', '讲师中心', '学生中心', '退出']
# school_list = ['创建课程', '招聘讲师', '创建班级', '退出']

from core.school_center import Manage_school
from core.teacher_center import Manage_teacher
from core.student_center import Manage_student
# School_center




# def file_oper(file, mode, *args):
#     if mode == 'wb':
#         data = args[0]
#         with open(file, mode) as f:
#             pickle.dump(data, f)
#     elif mode == 'rb':
#         with open(file, mode) as f:
#             data = pickle.load(f)
#             return data


def teacher_center():
    print('\033[35;1m讲师中心\033[0m')


def student_center():
    print('\033[35;1m学生中心\033[0m')

def init_database():
    pass



def main():
    while True:
        choice = file_oper.options(settings.main_list)
        if not choice: continue
        if choice == '1':
            m_school = Manage_school()
            m_school.run_manage()
        elif choice == '2':
            teacher_center()
            m_teacher = Manage_teacher()
            m_teacher.run_mange()
        elif choice == '3':
            # student_center()
            m_student = Manage_student()
            m_student.run_manage()
        elif choice == '4':
            break
        else:
            print('\033[31;1m错误：序号错误.\033[0m')
