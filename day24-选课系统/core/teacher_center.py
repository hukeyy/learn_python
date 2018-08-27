# -*- coding: utf-8 -*-
# Author: hkey
import os, sys
from conf import settings
from core.file_oper import file_oper, options

class Manage_teacher(object):
    def __init__(self):
        self.teacher_dict = dict()
        self.course_dict = dict()
        if os.path.exists(settings.db_main_file):
            self.school_db = file_oper(settings.db_main_file, 'rb')
        else:
            print('\033[31;1m错误：未创建学校，请先创建学校.\033[0m')
            exit()

        if os.path.exists(settings.db_teacher_file):
            self.teacher_db = file_oper(settings.db_teacher_file, 'rb')
        else:
            print('\033[31;1m错误：未招聘讲师，请先创建讲师信息.\033[0m')
            exit()

    def run_mange(self):
        for teacher in self.teacher_db:
            self.teacher_dict[teacher.name] = teacher
        print(self.teacher_dict)
        teacher_name = input('\033[34;1m输入要登录的讲师名：\033[0m')
        if teacher_name in self.teacher_dict:
            teacher = self.teacher_dict[teacher_name]
            grade = self.teacher_db[teacher]['grade']
            while True:
                choice = options(settings.teacher_list)
                # ["查看班级", "查看班级学员列表","返回" ]
                if choice == '1':
                    print('\033[33;1m讲师【%s】的班级信息\033[0m'.center(50, '#') % teacher_name)
                    print('\033[32;1m学校【%s】\t课程【%s】\t班级【%s】\033[0m' % (teacher.school, teacher.course,
                                                                       grade.name))
                    any = input('\033[34;1m输入任意键返回:\033[0m')

                elif choice == '2':
                    print('\033[33;1m讲师【%s】的学员信息\033[0m'.center(50, '#') % teacher_name)
                    if grade.student:
                        print('\033[34;1m班级【%s】\n学员【%s】\033[0m' % (grade.name, grade.student))
                    else:
                        print('\033[34;1m班级【%s】\n学员【None】\033[0m' % grade.name)
                    any = input('\033[34;1m输入任意键返回:\033[0m')

                elif choice == '3':
                    break
                else:
                    print('\033[31;1m错误：序号错误.\033[0m')

        else:
            print('\033[31;1m错误：讲师信息不存在.\033[0m')