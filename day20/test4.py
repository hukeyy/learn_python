# -*- coding: utf-8 -*-
# Author: hkey
import shelve, time
LOGIN_TIME_OUT = 5
db = shelve.open('user.db', writeback=True)

def regist():
    global db
    while True:
        name = input('用户名:').strip()
        if not name: continue
        if name in db:
            print('\033[31;1m用户名已存在.\033[0m')
            continue
        else:
            break
    pwd = input('密码:')
    db[name] = {'password': pwd, 'last_login_time': time.time()}
    print(db[name])

def login():
    global db
    name = input('用户名:').strip()
    pwd = input('密码:')
    try:
        password = db.get(name).get('password')
    except AttributeError as e:
        print('用户名不存在.')
        return
    if pwd == password:
        login_time = time.time()
        last_login_time = db[name].get('last_login_time')
        if login_time - last_login_time < LOGIN_TIME_OUT:
            print('用户已登录，上次登录时间[%s]'
                  % time.strftime('%Y-%m-%d %X', time.localtime(last_login_time)))
        db[name]['last_login_time'] = login_time
        print('welcome back.')
    else:
        print('\033[31;1m登录错误\033[0m')



def showmenu():
    global db

    flag = False
    while not flag:
        print('1. 注册\n'
              '2. 登录\n'
              '3. 退出')

        chosen = False
        while not chosen:
            try:
                choice = input('>>>').strip()
            except (EOFError, KeyboardInterrupt):
                choice = '3'
            print('\033[32;1m你的选择是[%s]\033[0m' % choice)

            if choice not in '123':
                print('\033[31;1m错误的选项，请重新输入.\033[0m')
            else:
                chosen = True

        if choice == '3': flag = True
        if choice == '1': regist()
        if choice == '2': login()

    db.close()

if __name__ == '__main__':
    showmenu()
