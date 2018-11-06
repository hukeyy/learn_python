#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


class Teacher(object):
    def __init__(self, teacher_name, course_obj):
        self.teacher_name = teacher_name
        self.course_obj = course_obj
        self.teacher_grade = {}

    def add_grade(self, grade_name, grade_obj):
        self.teacher_grade[grade_name] = grade_obj

    def cat_teacher(self):
        print('\033[32;1m课程【%s】\t讲师【%s】\033[0m' % (self.course_obj.course_name, self.teacher_name))
