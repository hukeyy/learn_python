# -*- coding: utf-8 -*-
# Author: hkey
import shelve, time, datetime

LOGIN_TIME_OUT = 60
db = shelve.open('user.db', writeback=True)

def newuser():
    global db

    while True:
        name = input('用户名:')
        if name in db:
            print('用户名已存在，请重新输入.')
            continue
        elif len(name) == 0:
            print('用户名不能为空，请重新输入.')
            continue
        else:
            break
    pwd = input('password:')
    db[name] = {'password': pwd, 'last_login_time': time.time()}
    print(db[name])

def olduser():
    global db
    name = input('用户名:').strip()
    if not db.get(name):
        print('\033[31;1m用户名不存在.\033[0m\n')
        return
    pwd = input('密码:').strip()
    password = db.get(name).get('password')

    # try:
    #     password = db.get(name).get('password')
    # except AttributeError as e:
    #     print('')

    if pwd == password:
        login_time = time.time()
        last_login_time = db.get(name).get('last_login_time')
        if login_time - last_login_time < LOGIN_TIME_OUT:
            print('\033[31;1m你已经登录，上次登录时间:[%s]\033[0m'
                  % time.strftime('%Y-%m-%d %X', time.localtime(last_login_time)))

        db[name]['last_login_time'] = login_time
        print('欢迎回来。')
    else:
        print('登录错误。')


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
                choice = input('>>>').strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = '3'
            print('\033[32;1m你的选择[%s]\033[0m' % choice)
            if choice not in '123':
                print('\033[31;1m错误的选项，请重试\033[0m')
            else:
                chosen = True
        if choice == '3': flag = True
        if choice == '1': newuser()
        if choice == '2': olduser()
    db.close()


if __name__ == '__main__':
    showmenu()


