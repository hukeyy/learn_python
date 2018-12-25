#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys
import pickle
from conf import settings
from modules.log import Logger


class Auth:
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def register(self):
        user_list = Auth.file_oper(settings.USER_LIST_FILE, 'r').split('\n')[:-1]
        if self.user not in user_list:
            Auth.file_oper(settings.USER_LIST_FILE, 'a', self.user+'\n')
            user_home_path = os.path.join(settings.HOME_PATH, self.user)
            if not os.path.isdir(user_home_path):
                os.makedirs(user_home_path)
            user_dict = {'user': self.user, 'pwd': self.pwd, 'home_path': user_home_path, 
                         'limit_size':settings.LIMIT_SIZE}
            user_pickle = pickle.dumps(user_dict)
            user_db_file = os.path.join(settings.DB_PATH, self.user) + '.db'
            Auth.file_oper(user_db_file, 'ab', user_pickle)
            Logger.info('[%s]注册成功.' % self.user)
            return '201'
        else:
            Logger.warning('[%s]注册用户名已存在.' % self.user)
            return '401'

    def login(self):
        user_list = Auth.file_oper(settings.USER_LIST_FILE, 'r').split('\n')[:-1]
        if self.user in user_list:
            user_db_file = os.path.join(settings.DB_PATH, self.user) + '.db'
            user_pickle = Auth.file_oper(user_db_file, 'rb')
            user_dict = pickle.loads(user_pickle)
            if self.user == user_dict['user'] and self.pwd == user_dict['pwd']:
                Logger.info('[%s]登录成功.' % self.user)
                return user_dict
        else:
            Logger.error('[%s]用户名不存在.' % self.user)










    @staticmethod
    def file_oper(file, mode, *args):
        if mode == 'a' or mode == 'ab':
            data = args[0]
            with open(file, mode) as f:
                f.write(data)
        elif mode == 'r' or mode == 'rb':
            with open(file, mode) as f:
                data = f.read()
                return data



