#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
from lxml import etree
import logging.handlers
import logging
import os, sys


class logger:
    root = etree.parse('config.xml').getroot()
    logpath = root.find('logpath').text
    logsize = 1024 * 1024 * int(root.find('logsize').text)
    lognum = int(root.find('lognum').text)
    logname = os.path.join(logpath, sys.argv[0].split('/')[-1].split('.')[0]) + '.log'
    log = logging.getLogger()
    fromater = logging.Formatter('[%(asctime)s][%(filename)s][%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

    handle1 = logging.handlers.RotatingFileHandler(logname, maxBytes=logsize, backupCount=lognum, encoding='utf-8')
    handle1.setFormatter(fromater)

    handle2 = logging.StreamHandler()
    handle2.setFormatter(fromater)
    log.addHandler(handle1)
    log.addHandler(handle2)

    log.setLevel(logging.INFO)

    @classmethod
    def info(cls, msg):
        cls.log.info(msg)

    @classmethod
    def warning(cls, msg):
        cls.log.warning(msg)

    @classmethod
    def error(cls, msg):
        cls.log.warning(msg)





