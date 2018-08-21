# -*- coding: utf-8 -*-
# Author: hkey
import pickle, os


class User(object):
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd
        self.user_info = {'name': self.name, 'passwd': self.passwd}

    @staticmethod
    def file_oper(file, mode, *arg):
        if mode == 'wb':
            with open(file, mode) as f:
                user_info = arg[0]
                pickle.dump(user_info, f)
        elif mode == 'rb':
            with open(file, mode) as f:
                data = pickle.load(f)
                return data

    def regist(self):
        data = User.file_oper('user_dict', 'rb')
        data.append(self.user_info)
        User.file_oper('user_dict', 'wb', data)

    def login(self):
        user_dict = User.file_oper('user_dict', 'rb')
        if self.user_info in user_dict:
            return True
        else:
            return False


def init_database():
    if not os.path.exists('user_dict'):
        user_list = []
        with open('user_dict', 'wb') as f:
            pickle.dump(user_list, f)


def start():
    while True:
        print('\033[32;1m欢迎使用系统\033[0m'.center(50, '#'))
        print('\033[33;1m1. 注册\n2. 登录\n3. 退出\033[0m')
        choice = input('\033[34;1m选择序号：\033[0m')
        if not choice: continue
        if choice == '1':
            name = input('name:').strip()
            passwd = input('passwd:').strip()
            user = User(name, passwd)
            user.regist()
        elif choice == '2':
            name = input('name:').strip()
            passwd = input('passwd:').strip()
            user = User(name, passwd)
            if user.login():
                print('\033[32;1m用户【%s】登录成功.\033[0m' % user.name)
            else:
                print('\033[31;1m登录失败。\033[0m')
        elif choice == '3':
            break
        else:
            print('\033[31;1m错误：序号错误.\033[0m')



if __name__ == '__main__':
    init_database()
    start()
