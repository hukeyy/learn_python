#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, json
from conf.settings import DB_PATH, HOME_PATH, USER_LIST_FILE
class Auth:
    def __init__(self, user, password):
        self.user = user
        self.pwd = password

    @staticmethod
    def user_oper(file, mode, *args):
        if mode == 'r':
            user_list = []
            with open(file, mode) as f:
                for line in f:
                    user_list.append(line)
            return user_list
        elif mode == 'a':
            user = args[0] + '\n'
            with open(file, mode) as f:
                f.write(user)

    def regist(self):
        user_list = Auth.user_oper(USER_LIST_FILE, 'r')
        if self.user not in user_list:
            Auth.user_oper(USER_LIST_FILE, 'a', self.user)
            home_path = os.path.join(HOME_PATH, self.user)
            if not os.path.isdir(home_path):
                os.makedirs(home_path)
            user_dict = {'name': self.user, 'password': self.pwd, 'home_path': home_path, 'quota': 102400}
            user_json = json.dumps(user_dict)
            user_home = os.path.join(DB_PATH, self.user)
            with open(user_home+'.json', 'a') as f:
                f.write(user_json)
            print('\033[32;1m注册成功。\033[0m')

        else:
            print('\033[31;1m该用户已存在.\033[0m')
    def login(self):
        pass
























