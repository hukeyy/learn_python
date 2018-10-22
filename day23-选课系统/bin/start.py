#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_DIR = os.path.join(BASE_DIR, 'db', 'school')
sys.path.append(BASE_DIR)

from core import main


if __name__ == '__main__':
    main.start()

