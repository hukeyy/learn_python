# -*- coding: utf-8 -*-
# Author: hkey
import os, sys
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)

from core import auth
from conf import settings

user_dict_file = os.path.join(settings.database_path, 'user_dict')


def init_user():
    user_dict = {'kind': '学生', 'username': 'hkey', 'passwd': '123'}
    with open(user_dict_file, 'wb') as f:
        pickle.dump(user_dict, f)


if __name__ == '__main__':
    init_user()
    print('\033[32;1m欢迎使用选课系统\033[0m'.center(50, '#'))
    user = input('\033[34;1m用户名：\033[0m')
    passwd = input('\033[34;1m密码：\033[0m')
    kind = input('类别：')

    auth = auth.Auth(user, passwd, kind)
    if auth.is_auth(user_dict_file):
        print('\033[32;1m用户【%s】登录成功.\033[0m' % auth.user)
    else:
        print('\033[31;1m登录失败.\033[0m')
