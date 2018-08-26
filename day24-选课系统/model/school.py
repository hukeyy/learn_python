#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def cat_school(self):
        print('\033[32;1m学校名：【%s】地址：【%s】\033[0m' % (self.name, self.addr))