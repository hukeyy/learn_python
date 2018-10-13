#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import time

true_time = time.strptime('2008-1-1 00:00:00', '%Y-%m-%d %H:%M:%S')
now_time = time.localtime(time.time())
print('2008-现在过去了%d年%d月%d日%d时%d分%d秒' % (now_time.tm_year - true_time.tm_year,
                                        now_time.tm_mon - true_time.tm_mon,
                                        now_time.tm_mday - true_time.tm_mday,
                                        now_time.tm_hour - true_time.tm_hour,
                                        now_time.tm_min - true_time.tm_min,
                                        now_time.tm_sec - true_time.tm_sec))
