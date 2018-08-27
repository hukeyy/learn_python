# -*- coding: utf-8 -*-
# Author: hkey
from core.file_oper import file_oper

class Grade(object):
    def __init__(self, name, course, teacher):
        student = set([])
        self.name = name
        self.course = course
        self.teacher = teacher
        self.student = student

    def cat_grade(self):
        print('\033[32;1m班级：【%s】\t课程：【%s】\t讲师：【%s】\033[0m' % (self.name, self.course, self.teacher))

    def add_student(self, student_name, dict, teacher, file):
        self.student.add(student_name)
        dict[teacher] = {'grade': self}
        file_oper(file, 'wb', dict)

