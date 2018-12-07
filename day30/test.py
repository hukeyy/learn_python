#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# import redis
#
# # conn = redis.Redis(host='192.168.118.15', port=26379, db='0')
# # r = conn.pipeline()
# # for i in range(10):
# #     r.set(i, 'Test')
# # r.execute()
#
# from redis.sentinel import Sentinel
#
# sentinel = Sentinel([('192.168.118.15', 26379),
#                      ('192.168.118.15', 26380),
#                      ('192.168.118.15', 26381)], socket_timeout = 0.5)
#
# master = sentinel.discover_master('mymaster')
# print('redis 主节点: ', master)
#
# slaves = sentinel.discover_slaves('mymaster')
# print('redis 从节点集群: ', slaves)
#
# # 使用主节点进行写入操作
# master = sentinel.master_for('mymaster', db=0)
# w_ret = master.set('foo', 'bar')
#
# # 使用从节点读取数据
# slave = sentinel.slave_for('mymaster', db=0)
# r_ret = slave.get('foo')
# print(r_ret)
#
# # 执行结果：
# # redis 主节点:  ('192.168.118.16', 6382)
# # redis 从节点集群:  [('192.168.118.16', 6379), ('192.168.118.16', 6380), ('192.168.118.16', 6381)]
# # b'bar'


from rediscluster import StrictRedisCluster
import sys


def redis_cluster():
    redis_nodes = [{'host': '192.168.118.15', 'port': 6379},
                   {'host': '192.168.118.15', 'port': 6380},
                   {'host': '192.168.118.15', 'port': 6381},
                   {'host': '192.168.118.15', 'port': 6382},
                   {'host': '192.168.118.15', 'port': 6383},
                   {'host': '192.168.118.15', 'port': 6384}]
    try:
        redisconn = StrictRedisCluster(startup_nodes=redis_nodes)
    except Exception as e:
        print("Connect Error!")
        sys.exit(1)
    # redisconn.set('name', 'hkey')
    # redisconn.set('age',18)
    print("name is: ", redisconn.get('name'))
    print("age  is: ", redisconn.get('age'))

redis_cluster()











































