#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


class School(object):
    def __init__(self, school_name, school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
        self.school_course = {}
        self.school_grade = {}
        self.school_teacher = {}
        