#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


class Grade(object):
    def __init__(self, grade_name, course_obj):
        self.grade_name = grade_name
        self.course_obj = course_obj
        self.grade_student = {}
