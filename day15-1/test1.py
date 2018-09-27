#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import time

for i in range(0, 101, 2):
    time.sleep(0.1)
    char_num = i//2
    per_str = '\r%s%% : %s\n' % (i, '*' * char_num) if i == 100 else '\r%s%% : %s' % (i, '*' * char_num)
    print(per_str, end='', flush=True)







