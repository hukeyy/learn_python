#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys, pickle
from conf import settings
from modules.log import Logger


class Auth:
    def __init__(self, user_info):
        type, self.user, self.pwd = user_info.split(':')

    def register(self):
        user_list = Auth.file_oper(settings.USER_LIST_FILE, 'r').split('\n')[:-1]
        if self.user not in user_list:
            Auth.file_oper(settings.USER_LIST_FILE, 'a', self.user+'\n')
            home_path = os.path.join(settings.HOME_PATH, self.user)
            if not os.path.isdir(home_path):
                os.makedirs(home_path)
            user_dict = {'user': self.user, 'pwd': self.pwd, 'home_path': home_path, 'limit_size': settings.LIMIT_SIZE}
            user_dict_pk = pickle.dumps(user_dict)
            user_info_file = os.path.join(settings.DB_PATH, self.user) + '.db'
            Auth.file_oper(user_info_file, 'ab', user_dict_pk)
            Logger.info('[%s]注册成功.' % self.user)
            return '201'
        else:
            Logger.warning('[%s]用户已存在.' % self.user)
            return '401'
    
    def login(self):
        user_list = Auth.file_oper(settings.USER_LIST_FILE, 'r').split('\n')[:-1]
        if self.user in user_list:
            user_info_file = os.path.join(settings.DB_PATH, self.user) + '.db'
            user_dict_pk = Auth.file_oper(user_info_file, 'rb')
            user_dict = pickle.loads(user_dict_pk)
            if self.user == user_dict['user'] and self.pwd == user_dict['pwd']:
                Logger.info('[%s]用户登录成功.' % self.user)
                return '200', user_dict
            else:
                Logger.warning('[%s]用户名或密码错误.' % self.user)
                return '400'

        else:
            Logger.warning('[%s]用户名或密码错误.' % self.user)
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


