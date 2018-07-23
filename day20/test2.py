# -*- coding: utf-8 -*-
# Author: hkey
import shelve, time, datetime

db = shelve.open('user_shelve.db', writeback=True)

def showmenu():
    global db
    flag = False
    while not flag:
        chosen = False
        while not chosen:
            print('1. 新用户登录\n'
                  '2. 老用户登录\n'
                  '3. 退出')
            try:
                choice = input('Enter choice:').strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = '3'
            print('\n你的选择是【%s】' % choice)
            if choice not in '123':
                print('\033[31;1m错误的选项，请重试\033[0m\n')
            else:
                chosen = True
        if choice == '3': flag = True
        if choice == '1': print('新用户登录\n')
        if choice == '2': print('老用户登录\n')
    db.close()

if __name__ == '__main__':
    showmenu()
