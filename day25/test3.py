# -*- coding: utf-8 -*-
# Author: hkey
with open('nginx.conf', 'rb') as f:
    data = f.read()
    print(data.decode().splitlines())
