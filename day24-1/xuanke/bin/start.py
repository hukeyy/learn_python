#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import sys, os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.main import Manage_center

if __name__ == '__main__':
    obj = Manage_center()
    obj.run()

