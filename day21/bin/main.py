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
        print('\033[32;1m学校名：【%s】，地址：【%s】\033[0m' % (self.name, self.addr))

    # school.create_course(dict_main, course, __db_main)
    def create_course(self, main_dict, course, file):
        main_dict[self][course] = {}
        file_oper(file, 'wb', main_dict)

    def hire_teacher(self, dict, course, teacher, file):
        dict[self][course] = {'teacher': teacher}
        file_oper(file, 'wb', dict)

    def create_grade(self, dict, teacher_dict, course, grade, teacher, file1, file2):
        # 数据库添加班级信息
        dict[self][course]['grade'] = grade
        file_oper(file1, 'wb', dict)
        teacher_dict[teacher] = {'grade': grade}
        file_oper(file2, 'wb', teacher_dict)


class Course(object):
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time

    def cat_course(self):
        print('\033[32;1m课程名：【%s】\t\t价格：【%s】\t\t周期：【%s个月】' % (self.name, self.price, self.time))


class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(People):
    def __init__(self, name, age, school, course, role='讲师'):
        super(Teacher, self).__init__(name, age)
        self.role = role
        self.school = school
        self.course = course

    def cat_teacher(self):
        print('课程：【%s】\t讲师：【%s】' % (self.course, self.name))


class Grade():
    # 创建班级
    def __init__(self, name, course, teacher):
        student = set([])
        self.name = name
        self.course = course
        self.teacher = teacher

    def cat_grade(self):
        # 查看班级信息
        print('\033[32;1m班级：【%s】\t课程：【%s】\t讲师：【%s】' % (self.name, self.course, self.teacher))


def file_oper(file, mode, *args):
    if mode == 'wb':
        with open(file, mode) as f:
            dict = args[0]
            pickle.dump(dict, f)
    elif mode == 'rb':
        with open(file, mode) as f:
            data = pickle.load(f)
            return data


def information(dict_data, mode, *args):
    if args:
        dict_info, set_info = {}, args[0]
    else:
        dict_info, set_info = {}, set([])

    if dict_data:
        for key in dict_data:
            if mode == 'main':
                key.cat_school()
            elif mode == 'course':
                key.cat_course()
            elif mode == 'teacher' and key == 'teacher':
                dict_data[key].cat_teacher()
                set_info.add(dict_data[key].name)
            elif mode == 'grade' and key == 'grade':
                dict_data[key].cat_grade()
                set_info.add(dict_data[key].name)

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
        dict_main = file_oper(__db_main, 'rb')
        # {'北京': <__main__.School object at 0x000001F5C36A5320>, '上海': <__main__.School object at 0x000001F5C36A5940>}
        res_dict = information(dict_main, 'main')[0]
        school_name = input('\033[34;1m输入要选择的学校：\033[0m').strip()
        if school_name in res_dict:
            # <__main__.School object at 0x0000027C4D9F5978>
            school = res_dict[school_name]
            while flag:
                print('\033[32;1m欢迎进入【%s】学校。\033[0m' % school_name)
                choice = options(list_school)
                # ["创建班级", "招聘讲师", "创建课程", "返回"]
                if choice == '1':
                    print('\033[42;1m【创建班级】\033[0m')
                    while True:
                        print('\033[32;1m学校【%s】目前已经有的班级信息\033[0m'.center(40, '#') % school.name)
                        teacher_dict = file_oper(__db_teacher, 'rb')
                        res_course = information(dict_main[school], 'None')[0]
                        set_info = set([])
                        if res_course:
                            for i in res_course:
                                k = res_course[i]
                                res_grade = information(dict_main[school][k], 'grade', set_info)[1]

                        if_cont = input('\033[34;1m是否要创建班级【y】创建【b】退出\033[0m').strip()
                        if if_cont == 'y':
                            grade_name = input('\033[34;1m输入要创建班级的名称：\033[0m:').strip()
                            course_name = input('\033[34;1m输入要班级上的课程：\033[0m:').strip()
                            if course_name in res_course:
                                course = res_course[course_name]
                                if dict_main[school][course]:
                                    teacher = dict_main[school][course]['teacher']
                                    if grade_name not in res_grade:
                                        grade = Grade(grade_name, course_name, teacher.name)
                                        school.create_grade(dict_main, teacher_dict, course, grade, teacher, __db_main,
                                                            __db_teacher)

                                    else:
                                        print('\033[31;1m错误：当前班级已经存在\033[0m')
                                else:
                                    print('\033[31;1m错误：当前课程还没有讲师\033[0m')

                            else:
                                print('\033[31;1m错误：课程【%s】不存在，请先创建课程\033[0m' % course_name)

                        elif if_cont == 'b':
                            break

                elif choice == '2':

                    print('\033[42;1m【招聘讲师】\033[0m')
                    while True:
                        print('\033[32;1m学校【%s】目前已经有的课程与讲师\033[0m'.center(40, '#') % school_name)
                        res_course = information(dict_main[school], 'None')[0]  # 取出课程的的类 {'linux':'class-linux'}
                        set_info = set([])
                        if res_course:
                            for i in res_course:
                                # print('i', i)
                                k = res_course[i]
                                # print('k', k)
                                # {class-school:{class-course:{class-teacher}}}
                                res_teacher = information(dict_main[school][k], 'teacher', set_info)[1]
                                # BUG: 多门课程，如果其中一门招聘了讲师，后面没有讲师的课程不会再显示出来
                                if not res_teacher:
                                    print('课程：【%s】\t讲师为【None】' % i)

                        if_cont = input('\033[34;1m是否要招聘讲师【y】招聘【b】退出\033[0m').strip()
                        if if_cont == 'y':
                            teacher_name = input('\033[34;1m输入要招聘讲师的名字：\033[0m').strip()
                            teacher_age = input('\033[34;1m输入要招聘讲师的年龄：\033[0m').strip()
                            course_name = input('\033[34;1m输入讲师【%s】要教授的课程：\033[0m' % teacher_name).strip()
                            if course_name in res_course:
                                course = res_course[course_name]  # 创建讲师写入数据库
                                if teacher_name not in res_teacher:
                                    teacher = Teacher(teacher_name, teacher_age, school.name, course_name)
                                    # hire_teacher(self, dict, course, teacher, file)
                                    school.hire_teacher(dict_main, course, teacher, __db_main)
                                else:
                                    print('\033[0m错误：教师【%s】已经被聘用\033[0m' % teacher_name)

                            else:
                                print('\033[31;1m错误：课程【%s】不存在，请先创建课程\033[0m' % course_name)


                        elif if_cont == 'b':
                            break

                elif choice == '3':
                    print('\033[42;1m【创建课程】\033[0m')
                    while True:
                        print('\033[32;1m学校【%s】目前已经有的课程\033[0m'.center(50, '#') % school_name)
                        # res_dict: {'python': < __main__.Course object at 0x00000200589F6E10 >
                        res_dict = information(dict_main[school], 'course')[0]  # 打印课程信息赋值给字典res_dict
                        if_cont = input('\033[34;1m是否要创建课程【y】创建【b】退出\033[0m:').strip()
                        if if_cont == 'y':
                            course_name = input('\033[34;1m输入要创建的课程：\033[0m').strip()
                            if course_name not in res_dict:
                                course_price = input('\033[34;1m输入课程【%s】课程价格：\033[0m' % course_name).strip()
                                course_time = input('\033[34;1m输入课程【%s】课程周期：\033[0m' % course_name).strip()
                                course = Course(course_name, course_price, course_time)
                                school.create_course(dict_main, course, __db_main)
                            else:
                                print('\033[31;1m错误：当前课程【%s】已经存在.\033[0m' % course_name)
                        elif if_cont == 'b':
                            break

                elif choice == '4':
                    flag = False
                else:
                    print('\033[31;1m序号错误，请重新输入.\033[0m')

        else:
            print('\033[31;1m输入的学校名不存在，请重新输入.\033[0m')


def init_database():
    sh = School('上海', '上海市')
    bj = School('北京', '北京市')
    if not os.path.exists(__db_main):
        with open(__db_main, 'wb') as f:
            dict = {sh: {}, bj: {}}
            pickle.dump(dict, f)
    if not os.path.exists(__db_teacher):
        with open(__db_teacher, 'wb') as f:
            dict = {}
            pickle.dump(dict, f)


def options(list):
    for k, v in enumerate(list, 1):
        print(k, v)
    choice = input('请选择模式：').strip()
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
            print('\033[31;1m序号错误，请重新输入。\033[0m')


if __name__ == '__main__':
    init_database()
    list_main = ["学生中心", "讲师中心", "学校中心", "退出"]
    list_school = ["创建班级", "招聘讲师", "创建课程", "返回"]
    list_teacher = ["查看班级", "查看班级学员列表", "返回"]
    list_student = ["学员注册", "返回"]
    start()
