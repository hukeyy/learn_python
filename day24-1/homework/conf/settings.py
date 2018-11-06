#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

main_db_file = os.path.join(BASE_DIR, 'db', 'main_dict')
teacher_db_file = os.path.join(BASE_DIR, 'db', 'teacher_dict')
