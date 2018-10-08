#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


# def auth(auth_type):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             username = input('username:').strip()
#             passwd = input('passwd:').strip()
#             if auth_type == 'filedb':
#                 print('filedb 验证中...')
#                 if username == 'hkey' and passwd == '123':
#                     res = func(*args, **kwargs)
#                     return res
#
#             elif auth_type == 'ldap':
#                 print('ldap 验证中...')
#                 if username == 'admin' and passwd == '123':
#                     res = func(*args, **kwargs)
#                     return res
#
#         return wrapper
#
#     return decorator
#
#
# @auth('ldap')
# def home():
#     print('\033[32;1mwelcome home.\033[0m')
#
#
# @auth('filedb')
# def shopping_cars():
#     print('\033[32;1mshopping cars \033[0m')
#
#
# shopping_cars()
# home()

import sys
sys.setrecursionlimit(10000000)

n = 0

def story():
    global n
    n +=1
    print(n)
    story()

story()






