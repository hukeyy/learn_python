# -*- coding: utf-8 -*-
# Author: hkey
import pickle

# db = {}
# db['hkey'] = {'name': 'hkey', 'age': 20}
#
# with open('test.txt', 'wb') as f:
#     pickle.dump(db, f)

with open('test.txt', 'rb') as f:
    data = pickle.load(f)

print(data)



