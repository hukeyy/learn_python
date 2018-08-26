#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os

from model import school
# class School(object):

from conf import settings
# db_path = os.path.join(BASE_DIR, 'database')
# main_list = ['学校中心', '讲师中心', '学生中心', '退出']
# school_list = ['创建课程', '招聘讲师', '创建班级', '退出']

school_file = os.path.join(settings.db_path, 'school_dict')

class School_center(object):
    def __init__(self):
        if not os.path.exists(school_file):
            sh = school.School('上海', '上海市')
            bj = school.School('北京', '北京市')


































