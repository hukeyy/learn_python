#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# class Foo(object):
#     def __init__(self, name, age):
#         self._name = name # 单下划线开始的成员变量叫做保护变量，只有类对象和子类对象自己能访问到这些变量
#         self.__age = age # 双下划线是私有成员，只有类的内部能调用，类对象能够访问，但是应该避免直接去访问
#
#
# f = Foo('hkey', 20)
# print(f.__dict__)   # 打印对象所有的属性和方法
# print(f._name)
#
# # 执行结果：
# # {'_Foo__age': 20, '_name': 'hkey'}
# # hkey

# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __len__(self):
#         return len(self.name)
# f = Foo('dddddddddddddddd')
# print(len(f))

# class A(object):
#     def __init__(self):
#         print('init')
#
#     def __new__(cls, *args, **kwargs):
#         print('new %s' %cls)
#         return object.__new__(cls, *args, **kwargs)
#
# A()
#
# # 执行结果：
# # new <class '__main__.A'>
# # init

# class Student(object):
#     def __init__(self, *args):
#         self.names = args
#
#     def __len__(self):
#         return len(self.names)
#
# s = Student('xiaofei', 'hkey', 'xiaoA')
#
# print(len(s))
#
# # 执行结果：
# # 3

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __repr__(self):
#         return 'Student object (name: %s)' % self.name
#     # __repr__ = __str__
#
# s = Student('hkey')
# print(s)
# # 用内置方法 str 和 repr 调用
# print(str(s))
# # print(repr(s))
#
# # 执行结果：
# # Student object (name: hkey)
# # Student object (name: hkey)
# # print(repr(s))执行结果：
# # Student object (name: hkey)

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, *args, **kwargs):
#         print('My name is %s.' % self.name)
#
# s = Student('hkey')
# s()
#
# # 执行结果：
# # My name is hkey.

import os, hashlib

class User(object):
    def __init__(self, name, passwd, file):
        self.name = name
        self.passwd = passwd
        self.file = file

    def options(self, mode):
        if hasattr(self, mode):
            func = getattr(self, mode)
            func()

    def regist(self):
        if self.file in os.listdir('.'):
            user_list = []
            user_info = self.file_oper('r')
            for user in user_info:
                username = user.strip().split(':')[0]
                user_list.append(username)
            if self.name in user_list:
                print('\033[31;1m用户名已存在.\033[0m')
        else:
            user_info = '%s:%s\n' %(self.name, self.passwd)
            self.file_oper('a', user_info)

    def login(self):
        user_dict = dict()
        user_info = self.file_oper('r')
        for user in user_info:
            username, password = user.strip().split(':')
            user_dict[username] = password
        if self.name in user_dict and self.passwd == user_dict[self.name]:
            print('\033[32;1m登录成功.\033[0m')
        else:
            print('\033[31;1m登录失败.\033[0m')

    def file_oper(self, mode, *args):
        if mode == 'a':
            with open(self.file, mode) as f:
                user_info = args[0]
                f.write(user_info)
        elif mode == 'r':
            with open(self.file, mode) as f:
                # user_info = f.read()
                user_info = f.readlines()
                return user_info


if __name__ == '__main__':
    while True:
        print('1. 注册\n'
              '2. 登录\n'
              '3. 退出')
        choice = input('>>>').strip()
        if choice == '3':
            break
        username = input('username:').strip()
        password = input('password:').strip()
        if choice == '1':
            user = User(username, password, 'user.txt')
            user.options('regist')
        elif choice == '2':
            user = User(username, password, 'user.txt')
            user.options('login')


























