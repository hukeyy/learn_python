# -*- coding: utf-8 -*-
# Author: hkey
import pickle
d = {'bj': '北京'}
# with open('test.db', 'wb') as f:
#     pickle.dump(d, f)

with open('test.db', 'rb') as f:
    data = pickle.load(f)

