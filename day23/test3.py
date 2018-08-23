#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


class Teacher(object):
    def __init__(self, name, age, birthday):
        self.name = name
        self.age = age
        self.birthday = birthday


class Birth(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


b = Birth(2000, 12, 12)

t = Teacher('xiaofei', 20, b)

print(t.birthday.day)
