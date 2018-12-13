#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys

BASE_DIR = os.getcwd()
sys.path.insert(0, BASE_DIR)
DATABASE_DIR = os.path.join(BASE_DIR, 'db')
USER_FILE = os.path.join(DATABASE_DIR, 'user.txt')
HOME_DIR = os.path.join(BASE_DIR, 'home')
LOG_PATH = os.path.join(BASE_DIR, 'log')
IP_PORT = ('localhost', 8080)
LOG_SIZE = 102400
LOG_NUM = 5
