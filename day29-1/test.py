#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import time

# print(time.time())
# print(time.time())
# print(time.localtime(time.time()))
# print(time.strftime('%Y%m%d %H:%M:%S', time.localtime(time.time())))

# time --> localtime --> strftime
# strptime --> mktime --> time

# now_time = time.strftime('%Y%m%d %H:%M:%S', time.localtime(time.time()))
# print(time.strptime(now_time, '%Y%m%d %H:%M:%S'))
# print(time.mktime(time.strptime(now_time, '%Y%m%d %H:%M:%S')))

import random

# print(random.random())
# print(random.randint(1, 10))
# print(random.randrange(1, 10))
# print(random.sample((1,2,3,4,5,6), 4))  # 第一个参数是可迭代对象，第二个参数是需要获取的元素个数, 返回一个list类型
# print(random.choice([1, 2, 'a', 4, 'b', 6])) # 参数为可迭代对象，随机返回其中一个元素
# print(random.uniform(1, 10))    # 返回一个范围中的浮点数
# item = [1,2, 3, 4, 5, 6, 7]
# random.shuffle(item)
# print(item)


# def v_code():
#     ran_code = ''
#     for i in range(4):
#         ran_int = random.randint(0, 9)
#         ran_alpha = chr(random.randint(65, 90))
#         s = str(random.choice((ran_int, ran_alpha)))
#         ran_code += s
#     return ran_code
#
#
# v = v_code()
# print(v)

# import os
# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
# print(os.makedirs(r'abc/hkey'))
# print(os.removedirs(r'abc/hkey'))
# print(os.rmdir(r'abc/hkey'))
# print(os.path.split(r'D:\Program Files (x86)\JetBrains\PyCharm 2018.2.2'))
# import sys, time
# for i in range(10):
#     sys.stdout.write('#')
#     sys.stdout.flush()
#     time.sleep(0.2)


import logging

# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# logger = logging.basicConfig(level=logging.DEBUG,
#                              format='%(asctime)s %(filename)s [%(lineno)d] %(message)s',
#                              # filename='test.log'
#                              )
#
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

import logging

# logging.basicConfig(level=logging.DEBUG,
#                             format='%(asctime)s %(filename)s %(lineno)d %(message)s',
#                             filename='test.log',
#                             filemode='a'
#                              )
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# logger = logging.getLogger()
# fh = logging.FileHandler('test.log', encoding='utf-8')
# ch = logging.StreamHandler()
#
# formatter = logging.Formatter('%(asctime)s %(filename)s [%(lineno)d] %(message)s')
#
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# logger.addHandler(fh)
# logger.addHandler(ch)
#
# logger.debug('debug message.')
# logger.info('info message.')
# logger.warning('warning message.')
# logger.error('error message.')
# logger.critical('critical message.')

import random, re

# r = random.choice('abcdefg')
# print(r)
# print(re.match('com','comwww.runcomoob').group())
# print(re.match('com','Comwww.runcomoob', re.I).group())


r = re.match('dcom','comwww.runcomoob')
print(r)

























