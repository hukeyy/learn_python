# -*- coding: utf-8 -*-
# Author: hkey
with open('haproxy.cfg', 'r') as file:
    for line in file:
        print(line.strip())
