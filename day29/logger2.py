#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import logging

class Logger(object):
    def __init__(self, path, clevel=logging.DEBUG, flevel=logging.DEBUG):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 设置cmd日志
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        sh.setLevel(clevel)

        # 设置文件日志
        fh = logging.FileHandler(path, encoding='utf-8')
        fh.setFormatter(formatter)
        fh.setLevel(flevel)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    logger = Logger('test2.txt', logging.INFO, logging.INFO)
    logger.info('hello world。')
    logger.error('wrong!')





