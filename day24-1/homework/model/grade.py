#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


class Grade(object):
    def __init__(self, name, course_obj):
        self.name = name
        self.course_obj = course_obj
        self.student = {}
