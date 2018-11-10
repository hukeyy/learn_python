#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.manage_center import Manage_center

if __name__ == '__main__':
    obj = Manage_center()
    obj.run()

