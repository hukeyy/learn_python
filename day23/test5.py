#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import shelve, time

LOGIN_TIME_OUT = 30
db = shelve.open('user.db', writeback=True)


def regist():
    while True:
        name = input('\033[34;1musername:\033[0m')
        if not name: continue
        if name in db:
            print('\033[32;1m用户名已存在.\033[0m')
        else:
            break

    pwd = input('\033[34;1mpassword:\033[0m').strip()
    db[name] = {'password': pwd, 'last_login_time': time.time()}


def login():
    name = input('\033[34;1musername:\033[0m').strip()
    pwd = input('\033[34;1mpassword:\033[0m').strip()

    try:
        password = db.get(name).get('password')
    except AttributeError as e:
        print('\033[31;1m错误：用户名不存在.\033[0m')
        return None

    if pwd == password:
        last_login_time = db[name].get('last_login_time')
        login_time = time.time()
        if login_time - last_login_time < LOGIN_TIME_OUT:
            print('\033[33;1m该用户已登录，上次登录时间：【%s】\033[0m'
                  % time.strftime('%Y-%m-%d %X', time.localtime(last_login_time)))
        db[name]['last_login_time'] = login_time
        print('\033[32;1m欢迎登录.\033[0m')
    else:
        print('\033[31;1m密码错误.\033[0m')


def showmenu():
    while True:
        print('\n1. 注册\n'
              '2. 登录\n'
              '3. 退出\n')

        choice = input('>>>').strip()
        if choice == '1':
            regist()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print('\033[31;1m错误：序号错误，请重新输入.\033[0m')


if __name__ == '__main__':
    showmenu()