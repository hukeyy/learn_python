#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, pickle, sys
from modules.log import Logger
from conf import settings


class Auth:
    def __init__(self, user_info):
        self.username, self.password, self.user_type = user_info.split(':')
        # self.start()
        # if hasattr(self, user_type):
        #     func = getattr(self, user_type)
        #     func()

    # def start(self):
    #     if hasattr(self, self.user_type):
    #         func = getattr(self, self.user_type)
    #         func()

    def register(self):
        if os.path.isfile(settings.USER_NAME_FILE):
            user_list = Auth.file_oper(settings.USER_NAME_FILE, 'r').split('\n')[:-1]
            print('user_list:', user_list)
            if self.username not in user_list:
                Auth.file_oper(settings.USER_NAME_FILE, 'a', self.username+'\n')
                user_home_path = os.path.join(settings.HOME_DIR, self.username)
                if not os.path.isdir(user_home_path):
                    os.makedirs(user_home_path)
                user_db_file = os.path.join(settings.DATABASE_DIR, self.username) + '.db'
                user_dict = {'username': self.username, 'password': self.password, 'home_path': user_home_path,
                             'limit_size': 1024000}
                user_info = pickle.dumps(user_dict)
                Auth.file_oper(user_db_file, 'ab', user_info)
                Logger.info('%s 注册成功.' % self.username)
                return '201'

            else:
                Logger.warning('[401][%s]用户名已存在，请重新注册.' % self.username)
                return '401'

        else:
            Logger.error('用户列表文件不存在，请先创建.')
            print('\033[31;1m用户列表文件不存在，请先创建.\033[0m')
            return '501'
            # sys.exit('用户列表文件不存在，请先创建.')

    def login(self):
        if os.path.isfile(settings.USER_NAME_FILE):
            user_list = Auth.file_oper(settings.USER_NAME_FILE, 'r').split('\n')[:-1]
            print('user_list:', user_list)
            if self.username in user_list:
                user_db_file = os.path.join(settings.DATABASE_DIR, self.username) + '.db'
                user_info = Auth.file_oper(user_db_file, 'rb', user_db_file)
                user_dict = pickle.loads(user_info)
                print('user_dict:', user_dict)
                if self.username == user_dict['username'] and self.password == user_dict['password']:
                    return '200', user_dict
            else:
                Logger.warning('[%s]用户名未注册.' % self.username)
                return '402'



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

