# -*- coding: utf-8 -*-
# Author: hkey
import shelve, time

LOGIN_TIMEOUT = 60
db = shelve.open('user.db', writeback=True)


def regist():
    print('\033[42;1m[regist]\033[0m')
    global db
    while True:
        name = input('username:').strip()
        if not name: continue
        if name in db:
            print('\033[31;1m该用户已存在.\033[0m')
            continue
        else:
            break
    pwd = input('password:').strip()
    db[name] = {'password': pwd, 'last_login_time': time.time()}
    print(db[name])


def login():
    print('\033[42;1m[login]\033[0m')
    global db
    name = input('username:').strip()
    pwd = input('password:').strip()
    try:
        password = db.get(name).get('password')
    except AttributeError as e:
        print('\033[31;1m该用户不存在\033[0m')
        return
    if pwd == password:
        login_time = time.time()
        last_login_time = db.get(name).get('last_login_time')
        if login_time - last_login_time < LOGIN_TIMEOUT:
            print('该用户已登录，登录时间 \033[32;1m[%s]\033[0m'
                  % time.strftime('%Y-%m-%d %X', time.localtime(last_login_time)))

        db[name]['last_login_time'] = login_time
        print('\033[32;1mwelcome back\033[0m')
    else:
        print('\033[31;1m登录错误\033[0m')


def showmenu():
    global db
    while True:
        print('1. 注册\n'
              '2. 登录\n'
              '3. 退出')
        choice = input('>>>').strip()
        if not choice: continue
        if choice == '3':
            break
        elif choice == '2':
            login()
        elif choice == '1':
            regist()
        else:
            print('\033[31;1m序号错误，请重新输入\033[0m')
            continue
    db.close()


if __name__ == '__main__':
    showmenu()
