#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
from model import course, grade

class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.course = {}
        self.grade = {}
        self.teacher = {}

    def create_course(self, course_name, course_price, course_time):
        course_obj = course.Course(course_name, course_price, course_time)
        self.course[course_name] = course_obj

    def create_grade(self, grade_name, course_obj):
        grade_obj = grade.Grade(grade_name, course_obj)
        self.grade[grade_name] = grade_obj
