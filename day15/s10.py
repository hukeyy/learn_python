# -*- coding: utf-8 -*-
# Author: hkey

def auth(auth_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            username = input('用户名：').strip()
            passwd = input('密码：').strip()
            if auth_type == 'filedb':
                print('filedb 验证中...')
                if username == 'filedb' and passwd == '123':
                    res = func()
                    return res
            elif auth_type == 'ldap':
                print('ldap 验证中...')
                if username == 'ldap' and passwd == '123':
                    res = func()
                    return res

        return wrapper

    return decorator

@auth('filedb')
def home():
    print('welcome home.')
@auth('ldap')
def shopping_cars():
    print('个人购物车.')
home()
shopping_cars()

# 运行结果：
# 用户名：filedb
# 密码：123
# filedb 验证中...
# welcome home.
# 用户名：ldap
# 密码：123
# ldap 验证中...
# 个人购物车.