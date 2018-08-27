# -*- coding: utf-8 -*-
# Author: hkey

class Teacher(object):
    def __init__(self, name, school, course, role='讲师'):
        self.name = name
        self.school = school
        self.course = course
        self.role = role

    def cat_teacher(self):
        print('\033[32;1m课程：【%s】\t讲师：【%s】\033[0m' % (self.course, self.name))


