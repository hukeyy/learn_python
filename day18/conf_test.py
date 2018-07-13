# -*- coding: utf-8 -*-
# Author: hkey
# import configparser
#
# config = configparser.ConfigParser()
# config['DEFAULT'] = {'ServerAliveInterval': '45',
#                       'Compression': 'yes',
#                      'CompressionLevel': '9'}
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'
# topsecret['ForwardX11'] = 'no'
# config['DEFAULT']['ForwardX11'] = 'yes'
#
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)

# import configparser
# config = configparser.ConfigParser()
# config.read('example.ini')
# print(config.sections())    # ['bitbucket.org', 'topsecret.server.com']
# print('bytebong.com' in config)     # False
# print(config['bitbucket.org']['User'])  # hg
# print(config['DEFAULT']['Compression'])     # yes
# print(config['topsecret.server.com']['ForwardX11'])     # no
#
# for key in config['bitbucket.org']:
#     print(key)
#
# # user
# # serveraliveinterval
# # compression
# # compressionlevel
# # forwardx11

# import configparser
#
# config = configparser.ConfigParser()
# config.read('example.ini')
# config.add_section('xiaofei')
# config['xiaofei'] = {
#     'name': 'xiaofei',
#     'age': 20
# }
#
# config.write(open('example.ini', 'w'))

# import configparser
#
# config = configparser.ConfigParser()
# config.read('example.ini')
# config.remove_section('bitbucket.org')      # 删除 [bitbucket.org] 下所有内容
# config.remove_option('xiaofei', 'name')     # 删除 [xiaofei] 下 name项
# config.set('xiaofei', 'age', '18')          # 修改 [xiaofei] age = 18 必须为str类型
# config.write(open('i.ini', 'w'))            # 保存修改内容
# config.default_section
























