# -*- coding: utf-8 -*-
# Author: hkey

import shelve

# writeback：为True时，当数据发生变化会回写，不过会导致内存开销比较大
d = shelve.open('test.db', writeback=True)
d['name'] = {'name':'hkey'}
d.sync()
print(d['name']) # {'name': 'hkey'}
d['name']['age'] = '20'
print(d['name'])  # {'name': 'hkey'}
d['name'] = 'xiaofei'
print(d['name']) # xiaofei
d.close()
