#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import logging,os
import ctypes

FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01 # text.txt color contains blue.
FOREGROUND_GREEN= 0x02 # text.txt color contains green.
FOREGROUND_RED  = 0x04 # text.txt color contains red.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN


STD_OUTPUT_HANDLE= -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool



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

    def warning(self, message, color=FOREGROUND_YELLOW):
        set_color(color)
        self.logger.warning(message)
        set_color(FOREGROUND_WHITE)

    def error(self, message, color=FOREGROUND_RED):
        set_color(color)
        self.logger.error(message)
        set_color(FOREGROUND_WHITE)


    def critical(self, message):
        self.logger.critical(message)

if __name__ =='__main__':
    logyyx = Logger('yyx.log',logging.DEBUG,logging.DEBUG)
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.warning('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.critical('一个致命critical信息')



