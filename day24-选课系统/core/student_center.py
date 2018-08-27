# -*- coding: utf-8 -*-
# Author: hkey
import os

from conf import settings
from core.file_oper import file_oper, options


class Manage_student(object):
    def __init__(self):
        self.school_dict = dict()
        self.course_dict = dict()
        if os.path.exists(settings.db_main_file):
            self.school_db = file_oper(settings.db_main_file, 'rb')
        else:
            print('\033[31;1m错误：未创建学校，请先创建学校.\033[0m')

        if os.path.exists(settings.db_teacher_file):
            self.teacher_db = file_oper(settings.db_teacher_file, 'rb')
        else:
            print('\033[31;1m错误：未招聘讲师，请先创建讲师信息.\033[0m')

    def run_manage(self):
        while True:
            choice = options(settings.student_list)
            if choice == '1':
                # print('学员注册')
                student_name = input('\033[34;1m输入注册学生名：\033[0m').strip()
                for school in self.school_db:
                    school.cat_school()
                    self.school_dict[school.name] = school
                school_name = input('\033[34;1m选择学校：\033[0m').strip()
                if school_name in self.school_dict:
                    school = self.school_dict[school_name]
                    if self.school_db[school]:
                        res_course = self.school_db[school]
                        for course in res_course:
                            course.cat_course()
                            self.course_dict[course.name] = course
                        course_name = input('\033[34;1m选择课程：\033[0m').strip()
                        if course_name in self.course_dict:
                            course = self.course_dict[course_name]
                            if self.school_db[school][course].get('grade'):
                                for i in self.teacher_db:
                                    if course.name == i.course:
                                        teacher = i
                                        grade = self.teacher_db[teacher]['grade']
                                print('\033[34;1m课程【%s】的费用为【%s】\033[0m' % (course.name, course.price))
                                if_pay = input('\033[34;1m是否支付当前费用【y】支付：\033[0m')
                                if if_pay == 'y':
                                    # add_student(self, student_name, dict, teacher, file)
                                    grade.add_student(student_name, self.teacher_db, teacher, settings.db_teacher_file)
                                    print('\033[32;1m选课成功.\033[0m')
                                    any = input('\033[34;1m输入任意键退出当前:\033[0m')

                            else:
                                print('\033[31;1m错误：班级信息不存在.\033[0m')
                        else:
                            print('\033[31;1m错误：输入的班级信息不存在.\033[0m')

                else:
                    print('\033[31;1m错误：学校信息不存在.\033[0m')

            elif choice == '2':
                break
            else:
                print('\033[31;1m错误：序号错误.\033[0m')
