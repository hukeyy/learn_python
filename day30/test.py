#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import redis

conn = redis.Redis(host='192.168.118.104', port=6379, db='0')
r = conn.pipeline()
for i in range(10000):
    r.set(i, 'Test')
r.execute()






















