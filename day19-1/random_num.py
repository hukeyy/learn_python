#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import random

def v_code():
    code = ''
    for i in range(5):
        num = random.randint(0,9)
        alf = chr(random.randint(65, 90))
        add = random.choice([num, alf])
        code += str(add)
        # code = ''.join([code, str(add)])
    return code

print(v_code())
