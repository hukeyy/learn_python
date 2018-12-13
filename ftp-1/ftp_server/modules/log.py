#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import logging.handlers
import os, sys
from conf import settings


class Logger:
    logger = logging.getLogger()
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
    log_name = os.path.join(settings.LOG_PATH, sys.argv[0].split('/')[-1].split('.')[0]) + '.log'
    fh = logging.handlers.RotatingFileHandler(log_name, maxBytes=settings.LOG_SIZE, backupCount=settings.LOG_NUM,
                                              encoding='utf-8')
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
        cls.logger.info(msg)

    @classmethod
    def error(cls, msg):
        cls.logger.info(msg)



