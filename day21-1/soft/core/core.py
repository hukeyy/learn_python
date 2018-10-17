#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import logging
import time
from conf import settings
from lib import read_ini

config=read_ini.read(settings.config_path)
logger=logging.getLogger(__name__)

current_user={'user':None,'login_time':None,'timeout':int(settings.user_timeout)}
def auth(func):
    def wrapper(*args,**kwargs):
        if current_user['user']:
            interval=time.time()-current_user['login_time']
            if interval < current_user['timeout']:
                return func(*args,**kwargs)
        name = input('name>>: ')
        password = input('password>>: ')
        if config.has_section(name):
            if password == config.get(name,'password'):
                logger.info('登录成功')
                current_user['user']=name
                current_user['login_time']=time.time()
                return func(*args,**kwargs)
        else:
            logger.error('用户名不存在')

    return wrapper

@auth
def buy():
    print('buy...')

@auth
def run():

    print('''
1. 购物
2. 查看余额
3. 转账
    ''')
    while True:
        choice = input('>>: ').strip()
        if not choice:continue
        if choice == '1':
            buy()



if __name__ == '__main__':
    run()