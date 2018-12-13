#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import pickle, os
from conf import settings
from modules.log import Logger

class Auth:
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        # self.user, self.pwd, type = user_info.split(':')
        # print(self.user, self.pwd, type)
        # if hasattr(self, type):
        #     getattr(self, type)()

    def register(self):
        user_list = self.file_oper(settings.USER_FILE, 'r').split('\n')[:-1]
        if self.user not in user_list:
            print('============================')
            user_info_db = os.path.join(settings.DATABASE_DIR, self.user) + '.db'
            user_home = os.path.join(settings.HOME_DIR, self.user)
            if not os.path.isdir(user_home):
                os.makedirs(user_home)
                self.file_oper(settings.USER_FILE, 'a', self.user+'\n')
                user_dict = {'user': self.user, 'pwd': self.pwd, 'home_path': user_home, 'limit_size': 102400}
                user_dict_pk = pickle.dumps(user_dict)
                self.file_oper(user_info_db, 'ab', user_dict_pk)
                Logger.info('%s 注册成功.' % self.user)
                return '200'
            else:
                Logger.warning('用户家目录已存在.')
                print('用户家目录已存在.')
                return '501'

        else:
            Logger.warning('用户名已存在.')
            print('用户名已存在')
            return '502'

    def login(self):
        pass


    def file_oper(self, file, mode, *args):
        if mode == 'a' or mode == 'ab':
            data = args[0]
            with open(file, mode) as f:
                f.write(data)
        elif mode == 'r' or mode == 'rb':
            with open(file, mode) as f:
                data = f.read()
                return data



