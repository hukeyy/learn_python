#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


class Course(object):
    def __init__(self, course_name, course_price, course_time):
        self.course_name = course_name
        self.course_price = course_price
        self.course_time = course_time

    # def show_course(self):
    #     print('\033[32;1m课程【%s】\t价格【%s元】\t周期【%s个月】\033[0m' %(self.course_name,
    #                                                          self.course_price, self.course_time))
