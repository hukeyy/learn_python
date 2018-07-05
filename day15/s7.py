# -*- coding: utf-8 -*-
# Author: hkey

user_dic = [
    {'name': 'hkey', 'passwd': '123'},
    {'name': 'xiaofei', 'passwd': '123'},
]
current_user = {'username': None, 'login': False}
def auth(auth_type='filedb'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_user['username'] and current_user['login']:
                res = func(*args, **kwargs)
                return res
            username = input('用户名:').strip()
            passwd = input('密码:').strip()
            if auth_type == 'filedb':
                for user_info in user_dic:
                    if username == user_info['name'] and passwd == user_info['passwd']:
                        res = func(*args, **kwargs)
                        return res
                else:
                    print('用户名密码错误。')

            if auth_type == 'ldap':
                print('什么鬼东西！')
        return wrapper
    return decorator

@auth('filedb')
def index():
    print('欢迎进入主页.')
@auth('ldap')
def home():
    print('欢迎回家')

def shopping_cars():
    print('个人购物车')

index()
home()
# shopping_cars()