#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
from modules.course import Course

class School(object):
    def __init__(self, school_name, school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
        self.school_course = {}
        self.school_grade = {}
        self.school_teacher = {}

    def create_course(self, course_name, course_price, course_time):
        course_obj = Course(course_name, course_price, course_time)
        self.school_course[course_name] = course_obj

    def show_course(self):
        for key in self.school_course:
            course_obj = self.school_course[key]
            print('\033[32;1m课程【%s】\t价格【%s元】\t周期【%s个月】\033[0m' % (
                course_obj.course_name, course_obj.course_price, course_obj.course_time))