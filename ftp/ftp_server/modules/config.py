#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import configparser
import os, sys

if os.path.isfile(os.path.join('conf', 'config.ini')):
    f_ini = os.path.join('conf', 'config.ini')
else:
    sys.exit('配置文件不存在。')


class Config:
    config = configparser.ConfigParser()
    config.read(f_ini)





    # @classmethod
    # def logpath(cls):
    #    return cls.config['log']['logpath']
    # @classmethod
    # def logsize(cls):
    #    return int(cls.config['log']['logsize'])
    # @classmethod
    # def lognum(cls):
    #    return int(cls.config['log']['lognum'])



