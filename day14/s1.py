# -*- coding: utf-8 -*-
# Author: hkey

# f = open('test.txt', 'r', encoding='utf-8')
# print('文件名：', f.name)
# print('是否已关闭：', f.closed)
# print('访问模式：', f.mode)
#
# # 执行结果：
# # 文件名： test.txt
# # 是否已关闭： False
# # 访问模式： r

# f = open('test.txt', 'r', encoding='utf-8')
# str1 = f.read(8)
# print(str1)
# print('光标当前位置：', f.tell())
# f.close()
#
# # 执行结果：
# # abcdefgh
# # 光标当前位置： 8

# f = open('test.txt', 'r', encoding='utf-8')
# # read 方法读取的是字符数，而不是字节数
# str1 = f.read(8)
# print('【读取前8个字符：】',str1)
# print('【当前光标的位置（单位字节）：】', f.tell())
# # 使用 seek 方法将光标一定到文件开始位置
# f.seek(0, 0)
#
# print('【当前光标的位置（单位字节）：】', f.tell())
# print('【读取文件所有内容：】', f.read())
#
# # 执行结果：
# # 【读取前8个字符：】 哪里有彩虹告诉我
# # 【当前光标的位置（单位字节）：】 24
# # 【当前光标的位置（单位字节）：】 0
# # 【读取文件所有内容：】 哪里有彩虹告诉我能不能把我的愿望还给我


# f = open('caihong.txt', 'r', encoding='utf-8')
# for i in f:
#     print(i.strip())

# # 三元表达式：
# name = 'xiaofeii'
#
# # 当 if name == 'xiaofei' 成立，res='keke', 否则 res='guagua'
# res = 'keke' if name == 'xiaofei' else 'guagua'
# print(res)

# # 列表解析：
# l = [x for x in range(10)]
# print(l)
#
# # 执行结果：
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # 三元表达式和列表解析连用
# l = [x for x in range(10) if x > 5]
# print(l)
#
# # 执行结果：
# # [6, 7, 8, 9]


# # 生成器表达式：
#
# g = (x for x in range(10))
# print(g)
# print(next(g))
#
# # 执行结果：
# # <generator object <genexpr> at 0x0000013F82BE5570>
# # 0
# import time
# start_time = time.time()
# l1 = list(range(100000000))
# print(sum(l1))
# print(time.time() - start_time)

# start_time = time.time()
# print(sum(x for x in range(100000000)))
# print(time.time() - start_time)


