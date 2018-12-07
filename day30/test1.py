#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

from rediscluster import StrictRedisCluster


redis_nodes = [{'host': '192.168.118.15', 'port': 6382},
               {'host': '192.168.118.15', 'port': 6383},
               {'host': '192.168.118.15', 'port': 6384},
               {'host': '192.168.118.15', 'port': 6379},
               {'host': '192.168.118.15', 'port': 6380},
               {'host': '192.168.118.15', 'port': 6381}]

redisconn = StrictRedisCluster(startup_nodes=redis_nodes)
print(redisconn.get('name'))
