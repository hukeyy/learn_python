#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import re

s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

def wipe(s):
    res = s.replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+')
    return res


def get(s):
    no_space_exp = re.sub(' ', '', s)
    res = re.split("(\([^()]+\))", no_space_exp, 1)
    return res


def add_num(s):
    s = wipe(s)
    num_list = re.findall("([+-]?\d+\.?\d*)", s)
    k = 0
    for i in num_list:
        k += float(i)

    return k


def mul(s):
    while True:
        res = re.split("(\d+\.?\d*[*/][+-]?\d+\.?\d*)", s, 1)
        if len(res) == 3 and '*' in res[1]:
            a, b, c = res
            d, e = b.split('*')
            res_b = float(d) * float(e)
            s = a + str(res_b) + c
        elif len(res) == 3 and '/' in res[1]:
            a, b, c = res
            d, e = b.split('/')
            res_b = float(d) / float(e)
            s = a + str(res_b) + c
        else:
            return add_num(s)


def counter(s):
    while True:
        res = get(s)
        if len(res) == 3:
            a, b, c = res
            res_b = mul(b)
            s = a + str(res_b) + c
        else:
            return mul(s)


c = counter(s)
print(c)
