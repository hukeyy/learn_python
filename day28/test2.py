#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import logging

logger = logging.getLogger()
fh = logging.FileHandler('test.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.debug('debug message.')
logger.info('info message.')
logger.warning('warning message.')
logger.error('error message.')
logger.critical('critical message.')
