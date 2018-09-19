#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# # 第一步：
# f = open('text.txt', 'a+', encoding='utf-8') # (file, 文件操作模式, 文件编码)
# # file_no = f.fileno()
# # print(file_no, type(file_no))
# # print(f.isatty())
# # f.seek(2)
# # f.seek(2)
# # print(f.read())
# # f.write('hahaadf')
# # print(f.read(1))
# # f.seek(0)
# print(f.write('jack'))
# f.seek(0)
# print(f.read())
#
#
# # print(f.writelines('你住的巷子里我租了一件公寓'))
# f.close()


# f = open('text.txt', 'r', encoding='utf-8')
# print(f.read())
# f.close()

# f = ''  # 全局要申明下 f 变量，不然 f.close() 会报黄
# try:
#     f = open('text.txt', 'r', encoding='utf-8')
#     print(f.read())
# finally:
#     if f:
#         f.close()


with open('text.txt', 'r', encoding='utf-8') as f:
    print(f.read())
print(f.closed) # 通过 closed 获取文件是否关闭，True关闭，False未关闭

# 执行结果：
# 总有一天总有一年会发现
# 有人默默的陪在你的身边
# 也许 我不该在你的世界
# 当你收到情书
# 也代表我已经走远
# True