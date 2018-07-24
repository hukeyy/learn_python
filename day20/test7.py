# -*- coding: utf-8 -*-
# Author: hkey8
import shelve

db = shelve.open('test.db', writeback=True)
db['hkey'] = {'name':'hkey', 'age': 20}
print(db['hkey'])
# 执行结果：
# {'name': 'hkey', 'age': 20}

db['hkey']['age'] = 30 # 修改age 为 30 , 修改后的数据为：db['hkey'] = {'name':'hkey', 'age': 30}
print(db['hkey'])
# writeback=True 开启回写，能够及时修改及时展现
# {'name': 'hkey', 'age': 30}

db.close()

