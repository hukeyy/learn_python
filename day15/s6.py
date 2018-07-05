# -*- coding: utf-8 -*-
# Author: hkey

# 全局变量
user_dic = [
    {'name': 'hkey', 'passwd': '123'},
    {'name': 'xiaofei', 'passwd': '123'},
]


current_user = {'username': None, 'login': False}
def login(func):
    def wrapper(*args, **kwargs):
        if current_user['username'] and current_user['login']:
            res = func(*args, **kwargs)
            return res
        username = input('用户名：').strip()
        passwd = input('密码：').strip()
        for user_info in user_dic:
            if username == user_info['name'] and passwd == user_info['passwd']:
                current_user['username'] = username
                current_user['login'] = True
                res = func(*args, **kwargs)
                return res
        else:
            print('用户密码错误。')

    return wrapper

@login
def index(name):
    print('welcome index [%s]' % name)

@login
def home():
    print('welcome home.')

@login
def shopping_cars():
    print('welcome cars.')

@login
def order():
    print('个人账单。')

index('admin')
home()
shopping_cars()
order()
