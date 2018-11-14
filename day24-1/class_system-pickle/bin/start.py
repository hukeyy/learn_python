#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
from conf.settings import school_db_file
from core.manage_center import Manage_center

if __name__ == '__main__':
    obj = Manage_center()
    obj.run()
