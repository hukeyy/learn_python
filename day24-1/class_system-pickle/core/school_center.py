#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys, pickle
from conf.settings import school_db_file, teacher_db_file
from modules.tools import file_oper

class School_center(object):
    def __init__(self):
        if not os.path.exists(school_db_file):
            self.init_school()
            self.manage_run()
        else:
            self.school_db = file_oper(school_db_file)
            self.manage_run()

    def init_school(self):
        