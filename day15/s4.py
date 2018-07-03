# -*- coding: utf-8 -*-
# Author: hkey

def login(func):
    def wrapper(*args, **kwargs):
        username = input('用户名:').strip()
        passwd = input('密码:').strip()
        if username == 'admin' and passwd == '123':
            res = func(*args, **kwargs)
            return res
        else:
            print('用户名密码错误.')

    return wrapper

# index = login(index)
@login
def index(username):
    print('[%s] 欢迎进入主页' % username)


@login
def home():
    print('个人家目录')


@login
def shopping_cars():
    print('个人购物车')


index('admin')
home()
shopping_cars()
