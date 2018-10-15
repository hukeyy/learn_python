#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import shelve, hashlib

db = shelve.open('user.db', writeback=True)


def regist():
    global db
    while True:
        username = input('username:').strip()
        if not username: continue
        if username in db:
            print('\033[31;1m错误：用户名已存在.\033[0m')
        else:
            break
    password = input('password:').strip()
    md5 = hashlib.md5()
    md5.update(password.encode())
    password_md5 = md5.hexdigest()
    db[username] = {'password': password_md5}


def login():
    global db
    username = input('username:').strip()
    password = input('password:').strip()
    md5 = hashlib.md5()
    md5.update(password.encode())
    password = md5.hexdigest()
    if username in db:
        password_md5 = db[username].get('password')
        if password == password_md5:
            print('\033[32;1m登录成功.\033[0m')


def showmenu():
    global db
    while True:
        print('1. 注册\n'
              '2. 登录\n'
              '3. 退出')
        choice = input('>>>').strip()
        if choice == '1':
            regist()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print('\033[31;1m序号错误.\033[0m')
    db.close()


if __name__ == '__main__':
    showmenu()
