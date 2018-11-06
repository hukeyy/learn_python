#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


class Grade(object):
    def __init__(self, grade_name, course_obj):
        self.grade_name = grade_name
        self.course_obj = course_obj
        self.grade_student = set([])


    def cat_grade(self):
        print('\033[32;1m班级【%s】\t课程【%s】\033[0m' % (self.grade_name, self.course_obj.course_name))

    def add_student(self, student_name):
        self.grade_student.add(student_name)
