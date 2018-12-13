#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
from modules.config import config
import os, sys
import logging.handlers


class logger:
    config = config()
    logpath = config['log']['logpath']
    logsize = int(config['log']['logsize'])
    lognum = int(config['log']['lognum'])
    logname = os.path.join(logpath, sys.argv[0].split('/')[-1].split('.')[0]) + '.log'
    logger = logging.getLogger()
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
    fh = logging.handlers.RotatingFileHandler(logname, maxBytes=logsize, backupCount=lognum, encoding='utf-8')
    ch = logging.StreamHandler()
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.setLevel(level=logging.INFO)

    @classmethod
    def info(cls, msg):
        cls.logger.info(msg)
        
    @classmethod
    def warning(cls, msg):
        cls.logger.warning(msg)
        
    @classmethod
    def error(cls, msg):
        cls.logger.error(msg)
    

if __name__ == '__main__':
    logger = logger()
    logger.info('haha')


