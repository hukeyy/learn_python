# -*- coding: utf-8 -*-
# Author: hkey
import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(filename)s %(message)s',
#     # filename='logg.txt',
#     # filemode='w'
# )
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# 执行结果：
# 2018-07-14 08:51:56,441 logging_test.py debug message
# 2018-07-14 08:51:56,441 logging_test.py info message
# 2018-07-14 08:51:56,441 logging_test.py warning message
# 2018-07-14 08:51:56,441 logging_test.py error message
# 2018-07-14 08:51:56,441 logging_test.py critical message

import logging

logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

# logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
# logger.addHandler(ch)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

##################################################
logger1 = logging.getLogger('mylogger')
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger('mylogger')
logger2.setLevel(logging.INFO)

logger1.addHandler(fh)
logger1.addHandler(ch)

logger2.addHandler(fh)
logger2.addHandler(ch)

logger1.debug('logger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.error('logger1 error message')
logger1.critical('logger1 critical message')

logger2.debug('logger2 debug message')
logger2.info('logger2 info message')
logger2.warning('logger2 warning message')
logger2.error('logger2 error message')
logger2.critical('logger2 critical message')

# 执行结果：
# logger warning message
# logger error message
# logger critical message
# 2018-07-14 09:41:03,604 - mylogger - INFO - logger1 info message
# 2018-07-14 09:41:03,604 - mylogger - WARNING - logger1 warning message
# 2018-07-14 09:41:03,604 - mylogger - ERROR - logger1 error message
# 2018-07-14 09:41:03,604 - mylogger - CRITICAL - logger1 critical message
# 2018-07-14 09:41:03,604 - mylogger - INFO - logger2 info message
# 2018-07-14 09:41:03,604 - mylogger - WARNING - logger2 warning message
# 2018-07-14 09:41:03,604 - mylogger - ERROR - logger2 error message
# 2018-07-14 09:41:03,604 - mylogger - CRITICAL - logger2 critical message











# 执行结果：
# 2018-07-14 09:30:39,054 - root - WARNING - logger warning message
# 2018-07-14 09:30:39,054 - root - ERROR - logger error message
# 2018-07-14 09:30:39,054 - root - CRITICAL - logger critical message
# 2018-07-14 09:30:39,054 - mylogger - INFO - logger1 info message
# 2018-07-14 09:30:39,054 - mylogger - INFO - logger1 info message
# 2018-07-14 09:30:39,055 - mylogger - WARNING - logger1 warning message
# 2018-07-14 09:30:39,055 - mylogger - WARNING - logger1 warning message
# 2018-07-14 09:30:39,055 - mylogger - ERROR - logger1 error message
# 2018-07-14 09:30:39,055 - mylogger - ERROR - logger1 error message
# 2018-07-14 09:30:39,055 - mylogger - CRITICAL - logger1 critical message
# 2018-07-14 09:30:39,055 - mylogger - CRITICAL - logger1 critical message
# 2018-07-14 09:30:39,055 - mylogger - INFO - logger2 info message
# 2018-07-14 09:30:39,055 - mylogger - INFO - logger2 info message
# 2018-07-14 09:30:39,055 - mylogger - WARNING - logger2 warning message
# 2018-07-14 09:30:39,055 - mylogger - WARNING - logger2 warning message
# 2018-07-14 09:30:39,055 - mylogger - ERROR - logger2 error message
# 2018-07-14 09:30:39,055 - mylogger - ERROR - logger2 error message
# 2018-07-14 09:30:39,055 - mylogger - CRITICAL - logger2 critical message
# 2018-07-14 09:30:39,055 - mylogger - CRITICAL - logger2 critical message

