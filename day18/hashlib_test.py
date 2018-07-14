# -*- coding: utf-8 -*-
# Author: hkey
# import hashlib
#
# m = hashlib.md5()
# m.update('hello'.encode('utf-8'))
# print(m.hexdigest())    # 5d41402abc4b2a76b9719d911017c592
# m.update('world'.encode('utf-8'))
# print(m.hexdigest())    # fc5e038d38a57032085441e7fe7010b0
#
# m2 = hashlib.md5()
# m2.update('helloworld'.encode('utf-8'))
# print(m2.hexdigest())   # fc5e038d38a57032085441e7fe7010b0

import hashlib

hash = hashlib.sha256('888'.encode('utf-8'))
hash.update('aliyun'.encode('utf-8'))
print(hash.hexdigest()) #da7ecd435e6e0930532c115e7fe48c38d0405aa79586b0275717a0ab0a85acd1
