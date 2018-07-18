# -*- coding: utf-8 -*-
# Author: hkey

import re

def remove_md(s):
    if '*' not in s and '/' not in s:
        return s
    else:
        k = re.search('-?[\d\.]+[\*\/]-?[\d\.]+', s).group()
        s = s.replace(k, )


def add_sub(s):
    pass


def basic_operation(s):
    s = s.replace(' ', '')
    return add_sub(remove_md(s))

def calculate(expression):
    if not re.search('\([^()]\)', expression):
        return basic_operation(expression)

