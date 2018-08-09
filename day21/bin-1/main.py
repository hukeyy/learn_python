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
        print('\033[32;1m学校名：【%s】\t地址【%s】\033[0m' % (self.name, self.addr))

    def create_course(self, main_dict, course, file):
        main_dict[self][course] = {}
        file_oper(file, 'wb', main_dict)


class Course(object):
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time

    def cat_course(self):
        print('\033[32;1m课程名：【%s】\t价格：【%s】\t周期：【%s个月】\033[0m' % (self.name, self.price, self.time))


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
        res_school = information(res_main, 'main')[0]
        school_name = input('\033[34;1m输入要选择的学校：\033[0m').strip()
        if school_name in res_school:
            school = res_school[school_name]
            print('\033[32;1m欢迎进入【%s】学校.\033[0m' % school_name)
            while flag:
                choice = options(list_school)
                if not choice:continue
                if choice == '1':
                    # ["创建班级", "招聘讲师", "创建课程", "返回"]
                    print('\033[42;1m【创建班级】\033[0m')
                elif choice == '2':
                    print('\033[42;1m【招聘讲师】\033[0m')
                elif choice == '3':
                    print('\033[42;1m【创建课程】\033[0m')
                    while True:
                        print('\033[32;1m学校【%s】目前已经有的课程\033[0m'.center(50, '#') % school_name)
                        res_course = information(res_main[school], 'course')[0]
                        if_cont = input('\033[34;1m是否创建课程【y】创建【b】退出.\033[0m').strip()
                        if if_cont == 'y':
                            course_name = input('\033[34;1m输入要创建的课程名：\033[0m').strip()
                            if course_name not in res_course:
                                course_price = input('\033[34;1m输入课程【%s】价格：\033[0m' % course_name).strip()
                                course_time = input('\033[34;1m输入课程【%s】周期：\033[0m' % course_name).strip()
                                course = Course(course_name, course_price, course_time)
                                school.create_course(res_main, course, __db_main)
                            else:
                                print('\033[31;1m课程已存在.\033[0m')
                        elif if_cont == 'b':
                            break


                elif choice == '4':
                    flag = False
                else:
                    print('\033[31;1m错误：序号错误，请重新输入.\033[0m')



        else:
            print('\033[31;1m错误：学校不存在，请重新输入.\033[0m')






def options(list):
    for k, v in enumerate(list, 1):
        print(k, v)
    choice = input('\033[34;1m请选择模式：\033[0m').strip()
    return choice

def start():
    while True:
        choice = options(list_main)
        if not choice: continue
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
    sh = School('上海', '上海市')
    bj = School('北京', '北京市')
    if not os.path.exists(__db_main):
        dict = {sh:{}, bj:{}}
        with open(__db_main, 'wb') as f:
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
