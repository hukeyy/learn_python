#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
from conf.settings import logfile
import logging


def logger():
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    fh = logging.FileHandler(logfile)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger



