# -*- coding: utf-8 -*-
# Author: hkey

def auth(func):
    def wrapper(*args, **kwargs):
        username = input('用户名:').strip()
        passwd = input('密码:').strip()
        if username == 'admin' and passwd == '123':
            res = func(*args, **kwargs)
            return res
        else:
            print('用户名密码错误！')

    return wrapper

@auth
def home():
    print('welcome home.')

home()

# 执行结果：
# （1）用户名密码正确
# 用户名:admin
# 密码:123
# welcome home.
#
# （2）用户名密码错误
# 用户名:admin
# 密码:111
# 用户名密码错误！