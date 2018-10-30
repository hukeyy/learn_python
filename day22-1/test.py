#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


# def person(name, hp, aggr, sex):
#     data = {
#         'name': name,
#         'hp': hp,
#         'aggr': aggr,
#         'sex': sex
#     }
#
#     def hit(g):
#         g['hp'] -= data['aggr']
#         print('%s 被打，掉了%s 的血。' % (g['name'], data['aggr']))
#
#     data['hit'] = hit
#     return data
#
#
# def dog(name, hp, aggr, dog_type):
#     data = {
#         'name': name,
#         'hp': hp,
#         'aggr': aggr,
#         'dog_type': dog_type
#     }
#
#     def bite(p):
#         p['hp'] -= data['aggr']
#         print('%s 被咬，掉了%s 的血。' % (p['name'], data['aggr']))
#
#     data['bite'] = bite
#     return data
#
#
# kk = person('人', 100, 5, 'male')
# gg = dog('狗狗', 100, 10, 'teddy')
#
# kk['hit'](gg)
# gg['bite'](kk)

# class Person:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def walk(self):
#         print('走走走.')
#
# p = Person('hkey', 20, 'male')  # 实例化 Person
#
# print('name:', p.name)
# print('age:', p.age)
# print('sex:', p.sex)
# print('walk:', p.walk)

# 执行结果：

# name: hkey
# age: 20
# sex: male
# walk: <bound method Person.walk of <__main__.Person object at 0x0000024A4E819400>>









































