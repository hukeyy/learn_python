#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

class Teacher:
    def __init__(self, name, age, brith):
        self.name = name
        self.age = age
        self.brith = brith


class Brith:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


brith = Brith(1998, 10, 23)

hkey = Teacher('hkey', 20, brith)

print(hkey.brith.year)
print(hkey.brith.month)
