#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def cat_school(self):
        print('学校名：【%s】\t地址：【%s】' %(self.name, self.addr))

class Course(object):
    def __init__(self, name, price, time):
        self.name = name
        self.price = price
        self.time = time

    def cat_course(self):
        print('课程名：【%s】\t价格：【%s元】\t周期：【%s个月】' %(self.name, self.price, self.time))


def init_database():
    pass











