#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
from model.course import Course
from model.grade import Grade
from model.teacher import Teacher

class School(object):
    def __init__(self, school_name, school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
        self.school_course = {}
        self.school_grade = {}
        self.school_teacher = {}

    def cat_school(self):
        print('\033[32;1m学校【%s】\t地址【%s】\033[0m' % (self.school_name, self.school_addr))
        
    def create_course(self, course_name, course_price, course_time):
        course = Course(course_name, course_price, course_time)
        self.school_course[course_name] = course
        
    def create_grade(self, grade_name, grade):
        # grade = Grade(grade_name, course_obj)
        self.school_grade[grade_name] = grade

    def hire_teacher(self, teacher_name, course_obj):
        teacher = Teacher(teacher_name, course_obj)
        self.school_teacher[teacher_name] = teacher

