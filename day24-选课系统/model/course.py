#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

class Course(object):
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time

    def cat_course(self):
        print('\033[32;1m课程：【%s】\t价格：【%s】\t周期：【%s个月】\033[0m'
              % (self.name, self.price, self.time))