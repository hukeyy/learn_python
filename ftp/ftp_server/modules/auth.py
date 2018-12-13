#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
from modules.log import logger
from conf import settings
import pickle, os

class Auth:
    logger = logger()

    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    # @staticmethod
    # def input_user_info():
    #     print('\n1. 注册\n2. 登录')
    #     while True:
    #         choice = input('>>>').strip()
    #         if not choice: continue
    #         if choice == '1':
    #             pass
    #         elif choice == '2':
    #             pass
    #         else:
    #             print('\033[31;1m序号错误，请重新输入.\033[0m')
    #         user = input('\033[34;1musername:\033[0m').strip()
    #         pwd = input('\033[34;1mpassword:\033[0m').strip()

    def regist(self):
        user_list = self.file_oper(settings.user_file, 'r').split('\n')[:-1]
        print(user_list)
        if self.user not in user_list:
            self.file_oper(settings.user_file, 'a', self.user+'\n')
            user_home_path = os.path.join(settings.home_path, self.user)
            user_db = os.path.join(settings.db_path, self.user) + '.db'
            print('user_db', user_db)
            if not os.path.isdir(user_home_path):
                os.makedirs(user_home_path)
                user_info = {'user': self.user, 'pwd': self.pwd, 'homepath': user_home_path, 'limitsize': 102400}
                user_inf_pk = pickle.dumps(user_info)
                self.file_oper(user_db, 'ab', user_inf_pk)
                print('\033[32;1m注册成功.\033[0m')
                logger.info('%s 注册成功.' % self.user)
            else:
                logger.warning('用户家目录已存在.')
        else:
            logger.warning('用户名已存在.')

    def login(self):
        user_list = self.file_oper(settings.user_file, 'r').split('\n')[:-1]
        if self.user in user_list:
            user_db = os.path.join(settings.db_path, self.user) + '.db'
            user_info_pk = self.file_oper(user_db, 'rb')
            user_info = pickle.loads(user_info_pk)
            user = user_info['user']
            pwd = user_info['pwd']
            if self.user == user and self.pwd == pwd:
                print('\033[32;1m登录成功.\033[0m')
                logger.info('用户%s登录成功.' % self.user)
                print(user_info)
                return user_info
            else:
                print('\033[31;1m登录失败.\033[0m')
                logger.warning('用户%s登录失败.' % self.user)
        else:
            print('\033[31;1m用户名不存在.\033[0m')
            logger.warning('用户%s不存在.' % self.user)
            
    def file_oper(self, file, mode, *args):
        if mode == 'a' or mode == 'ab':
            data = args[0]
            with open(file, mode) as f:
                f.write(data)
        elif mode == 'r' or mode == 'rb':
            with open(file, mode) as f:
                return f.read()

    def user_info(self):
        user_list = []
        with open(settings.user_file) as f:
            for i in f:
                user_list.append(i)
            return user_list





