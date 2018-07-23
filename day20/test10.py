# -*- coding: utf-8 -*-
# Author: hkey
import shelve

db = shelve.open('user.db', writeback=True)
# def showmenu():
#     global db
#     flag = False
#     while not flag:
#         print('1. 注册\n'
#               '2. 登录\n'
#               '3. 退出')
#         tag = False
#         while not tag:
#             try:
#                 choice = input('>>>').strip()[0].lower()
#             except (EOFError, KeyboardInterrupt):
#                 choice = '3'
#             if not choice: continue
#             if choice not in '123':
#                 print('\033[31;1m序号错误，重新输入.\033[0m')
#             else:
#                 tag = True
#
#         if choice == '3': flag = True
#         if choice == '1': regist()
#         if choice == '2': login()

def regist():
    print('\033[31;1mregist\033[0m')

def login():
    print('\033[31;1mlogin\033[0m')

def showmenu():
    global db
    flag = False
    while not flag:
        print('1. 注册\n'
              '2. 登录\n'
              '3. 退出')
        choice = input('>>>').strip()
        if len(choice) == 0: continue
        if choice == '1': regist()
        if choice == '2': login()
        if choice == '3': flag = True
    db.close()

if __name__ == '__main__':
    showmenu()