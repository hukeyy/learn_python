#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
from core.file_oper import file_oper
from conf import settings

class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def cat_school(self):
        print('\033[32;1m学校名：【%s】地址：【%s】\033[0m' % (self.name, self.addr))

    def create_course(self, db_main, course):
        '''创建课程'''
        db_main[self][course] = {}
        file_oper(settings.db_main, 'wb', db_main)
