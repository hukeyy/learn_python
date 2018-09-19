#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os


def file_oper(file, mode, *args):
    if mode == 'r':
        list_user = []
        with open(file, mode) as f:
            for line in f:
                list_user.append(line.strip())
            return list_user
    elif mode == 'a+':
        data = args[0]
        with open(file, mode) as f:
            f.write(data)


class User(object):
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd
        self.file = 'user.db'

    def regist(self):
        data = '%s|%s\n' % (self.name, self.passwd)
        file_oper(self.file, 'a+', data)
        if os.path.isfile('user.db'):
            print('\033[32;1m注册成功.\033[0m')

    def login(self):
        list_user = file_oper(self.file, 'r')
        print('list_user:', list_user)
        user_info = '%s|%s' % (self.name, self.passwd)
        if user_info in list_user:
            print('\033[32;1m登录成功.\033[0m')
        else:
            print('\033[31;1m登录失败.\033[0m')


def start():
    while True:
        print('1. 注册\n'
              '2. 登录\n'
              '3. 退出')

        choice = input('\033[34;1m>>>\033[0m').strip()
        if choice == '1':
            username = input('\033[34;1musername:\033[0m').strip()
            password = input('\033[34;1mpassword:\033[0m').strip()
            user = User(username, password)
            user.regist()
        elif choice == '2':
            username = input('\033[34;1musername:\033[0m').strip()
            password = input('\033[34;1mpassword:\033[0m').strip()
            user = User(username, password)
            user.login()
        elif choice == '3':
            break
        else:
            print('\033[31;1m错误：输入序号错误。\033[0m')


if __name__ == '__main__':
    start()
