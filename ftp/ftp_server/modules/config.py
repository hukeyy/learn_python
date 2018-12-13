#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import configparser
import os, sys


def config():
    BASE_DIR = os.path.dirname(os.getcwd())
    if os.path.isfile(os.path.join(BASE_DIR, 'conf', 'config.ini')):
        f_ini = os.path.join(BASE_DIR, 'conf', 'config.ini')
    else:
        sys.exit('配置文件不存在。')

    config = configparser.ConfigParser()
    config.read(f_ini)
    return config




    # @classmethod
    # def logpath(cls):
    #    return cls.config['log']['logpath']
    # @classmethod
    # def logsize(cls):
    #    return int(cls.config['log']['logsize'])
    # @classmethod
    # def lognum(cls):
    #    return int(cls.config['log']['lognum'])



