#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


class Teacher(object):
    def __init__(self, teacher_name, teacher_salary):
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_grade = {}

    def teacher_add_grade(self, grade_name, grade_obj):
        self.teacher_grade[grade_name] = grade_obj
        