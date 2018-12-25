#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os

BASE_DIR = os.path.dirname(os.getcwd())
HOME_PATH = os.path.join(BASE_DIR, 'home')
LOG_PATH = os.path.join(BASE_DIR, 'logs')
DB_PATH = os.path.join(BASE_DIR, 'db')

USER_LIST_FILE = os.path.join(BASE_DIR, 'conf', 'user.list')

LOG_SIZE = 102400
LOG_NUM = 5

LIMIT_SIZE = 1024000000

IP_PORT = ('localhost', 8080)























