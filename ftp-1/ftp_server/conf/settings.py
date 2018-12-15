#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys

BASE_DIR = os.path.dirname(os.getcwd())
sys.path.insert(0, BASE_DIR)

DATABASE_DIR = os.path.join(BASE_DIR, 'db')
HOME_DIR = os.path.join(BASE_DIR, 'home')
LOG_DIR = os.path.join(BASE_DIR, 'logs')
USER_NAME_FILE = os.path.join(BASE_DIR, 'conf', 'user.txt')

IP_PORT = ('localhost', 8080)

LOG_PATH = os.path.join(BASE_DIR, 'logs')
LOG_SIZE = 102400
LOG_NUM = 5

LIMIT_FILE = 1024000000

