#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import pickle
import os


def file_oper(file, mode, *args):
    if mode == 'wb':
        user_info = args[0]
        with open(file, mode) as f:
            pickle.dump(user_info, f)
    elif mode == 'rb':
        with open(file, mode) as f:
            user_info = pickle.load(f)
        return user_info


def regist(file, user_dict):
    while True:
        username = input('username:').strip()
        if not username: continue
        if username in user_dict:
            print('\033[31;1m错误：用户名已存在.\033[0m')
        else:
            break

    password = input('password:').strip()
    user_dict[username] = password
    file_oper(file, 'wb', user_dict)
    print('\033[32;1m注册成功.\033[0m')


def login(user_dict):
    while True:
        username = input('username:').strip()
        if not username: continue
        if username not in user_dict:
            print('\033[32;1m错误：用户名不存在.\033[0m')
        else:
            break
    password = input('password:').strip()
    if user_dict[username] == password:
        print('\033[32;1m登录成功.\033[0m')
    else:
        print('\033[31;1m密码错误.\033[0m')


def showmenu():
    if not os.path.isfile('user.db'):
        file_oper('user.db', 'wb', {})
    user_dict = file_oper('user.db', 'rb')
    while True:
        print('1. 注册\n'
              '2. 登录\n'
              '3. 退出')
        choice = input('>>>').strip()
        if choice == '1':
            regist('user.db', user_dict)
        elif choice == '2':
            login(user_dict)
        elif choice == '3':
            break
        else:
            print('\033[31;1m错误：输入错误.\033[0m')


if __name__ == '__main__':
    showmenu()
