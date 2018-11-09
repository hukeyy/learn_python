#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

from modules.course import Course
from modules.grade import Grade
from modules.teacher import Teacher
from modules.student import Student

class School(object):
    def __init__(self, school_name, school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
        self.school_course = {}
        self.school_grade = {}
        self.school_teacher = {}

    def create_course(self, course_name, course_price, course_time):
        coures_obj = Course(course_name, course_price, course_time)
        self.school_course[course_name] = coures_obj

    def show_course(self):
        for key in self.school_course:
            course_obj = self.school_course[key]
            print('\033[32;1m课程【%s】\t价格【%s元】\t周期【%s个月】\033[0m' % (course_obj.course_name,
                                                                  course_obj.course_price, course_obj.course_time))
    def show_grade_course(self):
        for key in self.school_grade:
            grade_obj = self.school_grade[key]
            course_obj = grade_obj.grade_course_obj
            print('\033[32;1m班级【%s】\t关联课程【%s】\t价格【%s】\t周期【%s个月】\t\033[0m' %(
                grade_obj.grade_name, course_obj.course_name, course_obj.course_price,
                course_obj.course_time
            ))


    def create_grade(self, grade_name, course_obj):
        grade_obj = Grade(grade_name, course_obj)
        self.school_grade[grade_name] = grade_obj

    def show_grade(self):
        for key in self.school_grade:
            grade_obj = self.school_grade[key]
            print('\033[32;1m班级【%s】\t关联的课程【%s】\033[0m' % (grade_obj.grade_name,
                                                          grade_obj.grade_course_obj.course_name))

    def create_teacher(self, teacher_name, teacher_salary, grade_name, grade_obj):
        teacher_obj = Teacher(teacher_name, teacher_salary)
        teacher_obj.teacher_add_grade(grade_name, grade_obj)
        self.school_teacher[teacher_name] = teacher_obj

    def update_teacher(self, teacher_name, grade_name, grade_obj):
        teacher_obj = self.school_teacher[teacher_name]
        teacher_obj.teacher_add_grade(grade_name, grade_obj)

    def show_teacher(self):
        print('show_teacher')
        for key in self.school_teacher:
            teacher_obj = self.school_teacher[key]
            grade_list = []
            for i in teacher_obj.teacher_grade:
                grade_list.append(i)
            print('\033[32;1m讲师【%s】\t薪资【%s】\t关联班级【%s】\033[0m' %(teacher_obj.teacher_name,
                                                                teacher_obj.teacher_salary,
                                                                grade_list))
    def create_student(self, student_name, student_age, grade_choice):
        student_obj = Student(student_name, student_age)
        grade_obj = self.school_grade[grade_choice]
        grade_obj.grade_student[student_name] = student_obj
        self.school_grade[grade_choice] = grade_obj

    def show_teacher_gradeinfo(self, teacher_name):
        teacher_obj = self.school_teacher[teacher_name]
        for i in teacher_obj.teacher_grade:
            grade_obj = self.school_grade[i]
            student_list = []
            for k in grade_obj.grade_student:
                student_list.append(k)
            print('\033[32;1m班级【%s】\t课程【%s】\t学员【%s】\033[0m' % (
                grade_obj.grade_name, grade_obj.grade_course_obj.course_name, student_list
            ))











