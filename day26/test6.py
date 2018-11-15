#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
# from math import pi
#
#
# class Circle(object):
#     def __init__(self, r):
#         self.__r = r
#     @property
#     def per(self):
#         return 2*pi*self.__r
#     @property
#     def area(self):
#         return pi * self.__r **2
#
# c = Circle(5)
# # print(c.area)
# # print(c.per)
#
# c.area = 123


# class Person(object):
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name + ' run.'
#
#     @name.setter
#     def name(self, new_name):
#         if new_name.isalpha():  # new_name 必须是有字母或汉字组成
#             self.__name = new_name
#     @name.deleter
#     def name(self):
#         print('\033[31;1m我要删除类中【__name】属性了.\033[0m')
#         del self.__name
#
#
# p = Person('hkey')
# del p.name


# class Goods(object):
#     dicount = 0.5
#
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price * Goods.dicount
#
#     @classmethod
#     def modify_discount(cls, new_discount):
#         cls.dicount = new_discount
#
# apple = Goods('apple', 10)
# pear = Goods('pear', 5)
# Goods.modify_discount(0.2)  # 打 0.2 折
# print(apple.price)
# print(pear.price)

# class Login(object):
#     def __init__(self, user, pwd):
#         self.user = user
#         self.pwd = pwd
#     def login(self):
#         pass
#
#     @staticmethod
#     def get_user_pwd():
#         user = input('输入用户名:')
#         pwd = input('输入密码:')
#         Login(user, pwd)
#
# Login.get_user_pwd()    # 进行登录

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# p = Person('hkey', 20)
#
# print(hasattr(p, 'name'))


# class Foo:
#     f = '类对静态变量'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hi(self):
#         print('hi, %s' % self.name)
#
#
# obj = Foo('xiaofei', 20)
#
# print(hasattr(obj, 'name'))
# print(hasattr(obj, 'say_hi'))
# print('------------------------------')
# print(getattr(obj, 'name'))
# func = getattr(obj, 'say_hi')
# func()
# print(getattr(obj, 'aaaaa', '不存在!'))
# print('------------------------------')
# setattr(obj, 'gender', 'female')
# print(obj.gender)
# print('------------------------------')
# setattr(obj, 'show_name', lambda self: self.name + 'er')
# print(obj.show_name(obj))


import os


class Manage_cmd(object):
    def run(self):
        while True:
            cmd = input('>>>').strip()
            if not cmd: continue
            if hasattr(self, cmd):
                getattr(self, cmd)()
            else:
                print('-bash: %s: command not found' % cmd)

    def ls(self):
        print(os.listdir('.'))

    def exit(self):
        exit(1)


cmd = Manage_cmd()
cmd.run()




























