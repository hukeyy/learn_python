#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import logging
#
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test1.log',
#                     filemode='a')
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# 创建一个logger
logger = logging.getLogger()

# 创建日志的目录和字符集
fh = logging.FileHandler('test.log', encoding='utf-8')

# 创建日志打印到控制台
ch = logging.StreamHandler()

# 创建日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 设置日志等级
logger.setLevel(logging.DEBUG)

# 为对象创建日志格式
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 将创建的对象添加到Handler
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('debug message.')
logger.info('info message.')
logger.warning('warning message.')
logger.error('error message.')
logger.critical('critical message.')





