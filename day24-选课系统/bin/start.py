#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)

from core import main

if __name__ == '__main__':
    main.main()