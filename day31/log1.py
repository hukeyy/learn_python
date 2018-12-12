#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import logging
import logging.handlers

class logger:
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    # fh = logging.FileHandler('log.txt')
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh = logging.handlers.RotatingFileHandler('log.txt', encoding='utf-8')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)

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
    logger.info('哈哈')
