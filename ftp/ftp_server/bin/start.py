#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys

BASE_DIR = os.path.dirname(os.getcwd())
sys.path.insert(0, BASE_DIR)
from model.auth import Auth

if __name__ == '__main__':
    user = input('user:')
    pwd = input('pwd:')
    obj = Auth(user, pwd)
    obj.login()



































