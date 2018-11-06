#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

from core.school_center import School_center
from core.student_center import Student_center
from core.teacher_center import Teacher_center
from model.tools import option


def run():
    main_list = ['学校中心', '讲师中心', '学员中心', '退出']
    while True:
        choice = option(main_list)
        if choice == '1':
            School_center()
        elif choice == '2':
            Teacher_center()
        elif choice == '3':
            Student_center()
        elif choice == '4':
            break




















