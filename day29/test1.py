#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import logging
from logger import Logger

logxyz = Logger('test1.txt', logging.DEBUG, logging.DEBUG)

logxyz.debug('debug message.')
logxyz.info('info message.')
logxyz.warning('warning message.')
logxyz.error('error message.')
logxyz.critical('critical message.')




