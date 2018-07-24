# -*- coding: utf-8 -*-
# Author: hkey
import shelve, time

LOGIN_TIMEOUT = 5  # 登录超时时间，设置短点是为了方便测试
db = shelve.open('user.db', writeback=True)  # 实例化一个 shelve 的对象 db 用来持久化字典类型


def regist():
    '''
    注册函数，持久存储在对象 db
    :return: None
    '''
    global db  # 获取全局变量
    print('\033[32;1m[regist]\033[0m')
    while True:
        name = input('username:').strip()
        if not name:
            print('用户名不能为空.')
            continue
        elif name in db:
            print('\033[31;1m用户名已存在.\033[0m')
            continue
        else:
            break
    pwd = input('password:').strip()
    # 用户注册数据持久化存储
    db[name] = {'password': pwd, 'last_login_time': time.time()}


def login():
    '''
    用户登录，用户登录数据从db中匹配
    :return: None
    '''
    global db  # 获取全局变量
    print('\033[32;1m[login]\033[0m')
    name = input('username:').strip()
    pwd = input('password:').strip()
    try:
        # 通过 try...except 一次性检查用户名和密码，如果出现异常AttributeError表示用户名不存在
        password = db.get(name).get('password')
    except AttributeError as e:
        print('\033[31;1m用户名不存在.\033[0m')
        return
    if pwd == password:
        login_time = time.time()  # 获取登录成功时间
        last_login_time = db[name].get('last_login_time')  # 从db中获取上次登录时间
        if login_time - last_login_time < LOGIN_TIMEOUT:  # 如果两次登录时间间隔小于LOGIN_TIMEOUT，则提示已登录。
            print('\033[32;1m该用户已登录，上次登录时间[%s]'
                  % time.strftime('%Y-%m-%d %X', time.localtime(last_login_time)))
        db[name]['last_login_time'] = login_time  # 保存本次登录时间
        print('\033[32;1mwelcome back\033[0m')
    else:
        print('\033[31;1m登录错误\033[0m')


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
    db.close()


if __name__ == '__main__':
    showmenu()
