# -*- coding: utf-8 -*-
# Author: hkey

import re

# ret = re.search('<(?P<tag_name>\w+)>\w+</(?P=tag_name)>', '<h1>hello</h1>')
# #还可以在分组中利用?<name>的形式给分组起名字
# #获取的匹配结果可以直接用group('名字')拿到对应的值
# if ret:
#     print(ret.group('tag_name'))
#     print(ret.group())

# 执行结果：
# h1
# <h1>hello</h1>


# ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
# #如果不给组起名字，也可以用\序号来找到对应的组，表示要找的内容和前面的组内容一致
# #获取的匹配结果可以直接用group(序号)拿到对应的值
# print(ret.group(1))
# print(ret.group())
#
# #结果 ：<h1>hello</h1>

# import re
# # 匹配整数或小数并以整数显示
# res = re.findall('\d+\.\d*|(\d+)', '1-2*(60+(-40.35/5)-(-4*3))')
#
# print('', res)
# res.remove('')
# print(res)
#
# # 执行结果：
# # ['1', '2', '60', '', '5', '4', '3']
# # ['1', '2', '60', '5', '4', '3']

































