#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys

from modules import auth
BASE_DIR = os.path.dirname(os.getcwd())

sys.path.insert(0, BASE_DIR)


if __name__ == '__main__':
    user = input('user:')
    pwd = input('pwd:')
    cmd = input('>>>')
    auth = auth.Auth(user, pwd)
    if cmd == '1':
        auth.regist()
    elif cmd == '2':
        auth.login()


