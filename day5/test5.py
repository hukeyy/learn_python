#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import pickle
# data = {'name':'hkey', 'price': 200}
file = 'abc.db'
# with open(f, 'wb') as f:
#     pickle.dump(data, f)

with open(file, 'rb') as f:
    data = pickle.load(f)

print(data, type(data))





