#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# class Person:
#     language = ['Chinese',]
#
#     def __init__(self, name, age, job):
#         self.name = name
#         self.age = age
#         self.job = job
#
#
# hkey = Person('hkey', 20, 'it')
# jay = Person('jay', 20, 'singer')
#
# print(Person.language)
# hkey.language[0] = 'English'
# print(hkey.language)
# print(jay.language)
# print(Person.language)
#
# # 执行结果：
# # Chinese
# # English
# # Chinese

class Count:
    count = 0
    def __init__(self):
        Count.count += 1


a = Count()
b = Count()
print(a.count)
















