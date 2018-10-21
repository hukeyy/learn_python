#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import pickle, os
from conf import settings
from model import school


def file_oper(file, mode, *args):
    if mode == 'wb':
        data = args[0]
        with open(file, mode) as f:
            pickle.dump(data, f)
    elif mode == 'rb':
        with open(file, mode) as f:
            data = pickle.load(f)
            return data


def init_database():
    sh = school.School('北京', '北京市')
    bj = school.School('上海', '上海市')
    if not os.path.exists(settings.school_db_file):
        dic = {sh: {}, bj: {}}
        file_oper(settings.school_db_file, 'wb', dic)

