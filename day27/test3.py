#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# with open('test.txt', 'w') as f:
#     f.write('hello world.')
def regist():
    while True:
        user = input('user:')
        pwd = input('pwd:')

        user_info = '%s|%s\n' %(user, pwd)
        with open('test.txt', 'a') as f:
            f.write(user_info)

def login():
    user_dict = dict()
    with open('test.txt', 'r') as f:
        user_info = f.readlines()
    for user in user_info:
        username, password = user.strip().split('|')
        user_dict[username] = password

    print(user_dict)
    while True:
        user = input('user:')
        if not user: continue
        # if user in user_dict:
        #     print('\033[31;1m用户名已存在.\033[0m')
        pwd = input('pwd:')
        if user in user_dict and pwd == user_dict[user]:
            print('\033[32;1m登录成功.\033[0m')
            break
        else:
            print('\033[31;1m登录失败.\033[0m')


# regist()
login()





