#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_path = os.path.join(BASE_DIR, 'database')
main_list = ['学校中心', '讲师中心', '学生中心', '退出']
school_list = ['创建课程', '招聘讲师', '创建班级', '退出']

