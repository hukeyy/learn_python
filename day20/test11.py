# -*- coding: utf-8 -*-
# Author: hkey

def regist():
    pass

def login():
    pass

def showmenu():
    flag = False
    while not flag:
        print('1. 注册\n'
              '2. 登录\n'
              '3. 退出')
        tag = False
        while not tag:
            try:
                choice = input('>>>').strip()
            except (EOFError, KeyboardInterrupt):
                choice = '3'
            if not choice: continue
            if choice not in '123':
                print('\033[31;1m序号错误，请重新输入\033[0m')
            else:
                tag = True

        if choice == '3': flag = True
        if choice == '2': login()
        if choice == '1': regist()

