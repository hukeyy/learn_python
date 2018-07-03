# -*- coding: utf-8 -*-
# Author: hkey

login_stat = {'username': None, 'login': False}



def login(func):

    def wrapper(*args, **kwargs):
        username = input('用户名：')
        passwd = input('密码：')

        return func(*args, **kwargs)

    return wrapper




def index(username):
    print('%s 欢迎购物')

def home():
    print('个人家目录')

def shopping_car():
    print('购物车')