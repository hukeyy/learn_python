#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

from core.school_center import School_center
from model.tools import option


def run():
    main_list = ['学校中心', '讲师中心', '学员中心', '退出']
    while True:
        choice = option(main_list)
        if choice == '1':
            School_center()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            break




















