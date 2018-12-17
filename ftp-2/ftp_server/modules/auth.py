#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys
import pickle
from modules.log import Logger
from conf import settings


class Auth:
    def __init__(self, auth_info):
        auth_type, self.user, self.pwd = auth_info.split(':')

    def register(self):
        user_list = Auth.file_oper(settings.USER_LIST_FILE, 'r').split('\n')[:-1]
        if self.user not in user_list:
            Auth.file_oper(settings.USER_LIST_FILE, 'a', self.user+'\n')
            user_home_path = os.path.join(settings.HOME_PATH, self.user)
            if not os.path.isdir(user_home_path):
                os.makedirs(user_home_path)
            user_dict = {'user': self.user, 'pwd': self.pwd, 'home_path': user_home_path,
                         'limit_size': settings.LIMIT_SIZE}
            user_info_pk = pickle.dumps(user_dict)
            user_db = os.path.join(settings.DB_PATH, self.user) + '.db'
            Auth.file_oper(user_db, 'ab', user_info_pk)
            Logger.info('用户[%s]注册成功.' % self.user)
            return '201'

        else:
            Logger.warning('注册的用户名[%s]已存在.' % self.user)
            return '401'

    def login(self):
        user_list = Auth.file_oper(settings.USER_LIST_FILE, 'r').split('\n')[:-1]
        if self.user in user_list:
            user_db_file = os.path.join(settings.DB_PATH, self.user) + '.db'
            if os.path.isfile(user_db_file):
                user_info = Auth.file_oper(user_db_file, 'rb')
                user_dict = pickle.loads(user_info)
                if self.user == user_dict['user'] and self.pwd == user_dict['pwd']:
                    Logger.info('[%s]登录成功.' % self.user)
                    return '200'
                return '400'
        else:
            Logger.error('[%s:%s]用户名或密码错误.' % (self.user, self.pwd))
            return '400'



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


























