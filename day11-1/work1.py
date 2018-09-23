#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# def auth(func):
#     def wrapper(*args, **kwargs):
#         user = input('username:').strip()
#         pwd = input('password:').strip()
#         if user == 'admin' and pwd == '123':
#             print('\033[32;1mhello,%s\033[0m' % user)
#             func(*args, **kwargs)
#         else:
#             print('\033[31;1m认证错误！\033[0m')
#
#     return wrapper
#
#
# @auth
# def home():
#     print('welcome home.')
#
#
# home()


# （2）使用装饰器实现登录功能，当调用 home 函数时，验证方式为 filedb ，当登录购物车时，验证方式为 ldap

# def auth(type):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             user = input('username:').strip()
#             pwd = input('password:').strip()
#             if type == 'filedb':
#                 if user == 'filedb' and pwd == '123':
#                     ret = func(*args, **kwargs)
#                     return ret
#                 else:
#                     print('\033[31;1m登录失败\033[0m')
#             elif type == 'ldap':
#                 if user == 'ldap' and pwd == '123':
#                     ret = func(*args, **kwargs)
#                     return ret
#                 else:
#                     print('\033[31;1m登录失败\033[0m')
#             else:
#                 print('\033[31;1m错误：未知类型\033[0m')
#         return wrapper
#     return decorator
#
#
# @auth('filedb')
# def home():
#     print('welcome home')
#
# @auth('ldap')
# def shopping_car():
#     print('welcome shopping')
#
# # home()
# shopping_car()



























