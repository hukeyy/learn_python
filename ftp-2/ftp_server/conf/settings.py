#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os

BASE_DIR = os.path.dirname(os.getcwd())

DB_PATH = os.path.join(BASE_DIR, 'db')
LOG_PATH = os.path.join(BASE_DIR, 'logs')
HOME_PATH = os.path.join(BASE_DIR, 'home')
USER_LIST_FILE = os.path.join(BASE_DIR, 'conf', 'user.list')


LOG_SIZE = 102400
LOG_NUM = 5

LIMIT_SIZE = 10240000

IP_PORT = ('localhost', 8080)
























