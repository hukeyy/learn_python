# -*- coding: utf-8 -*-
# Author: hkey
import shelve, time

LOGIN_TIME_OUT = 30
db = shelve.open('user.db', writeback=True)

def regist():
    print('\033[32;1m[regist]\033[0m')
    while True:
        name = input('username:').strip()
        if not name:
            print('\033[31;1m用户名不能为空\033[0m')
            continue
        elif name in db:
            print('\033[31;1m用户名已存在\033[0m')
            continue
        else:
            break
    pwd = input('password:').strip()
    db[name] = {'password': pwd, 'last_login_time': time.time()}
    print(db[name])


def login():
    print('\033[32;1m[login]\033[0m')
    name = input('username:').strip()
    pwd = input('password:').strip()
    try:
        password = db.get(name).get('password')
    except AttributeError as e:
        print('\033[31;1m用户名不存在.\033[0m')
        return
    if pwd == password:
        login_time = time.time()
        last_login_time = db[name].get('last_login_time')
        if login_time - last_login_time < LOGIN_TIME_OUT:
            print('\033[33;1m该用户已登录，上次登录时间[%s]\033[0m'
                  % time.strftime('%Y-%m-%d %X', time.localtime(last_login_time)))
        db[name]['last_login_time'] = login_time
        print('\033[32;1mwelcome back\033[0m')
    else:
        print('\33[31;1m登录错误.\033[0m')


def showmenu():
    while True:
        print('1. 注册\n'
              '2. 登录\n'
              '3. 退出')

        choice = input('>>>').strip()
        if not choice: continue
        if choice == '1':
            regist()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print('\033[31;1m序号错误，请重新输入.\033[0m')


if __name__ == '__main__':
    showmenu()
