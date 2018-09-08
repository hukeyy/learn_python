# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
# # Author: hkey
#
# # 作业题：
# # 1. 使用while循环输入1,2,3,4,5,6 8,9,10
#
# count = 0
# while count < 10:
#     count += 1  # 等价于 count = count + 1
#     if count == 7:
#         continue  # continue 结束本次循环，开始下一次循环，continue 以下的代码都不再执行
#     print(count)
#
# # 2. 求 1-100 的所有数的和
#
# num = 0
# for i in range(1, 101):  # range取一个范围 1, 100的所有数字，通过for循环遍历相加
#     num += i
# print(num)
#
# # 3. 输出 1-100 的所有奇数
# print(list(range(1, 101, 2)))
# # 4. 输出 1-100 的所有偶数
# print(list(range(2, 101, 2)))
# # 5. 1-2+3-4+5 ...99的所有数的和
# sum = 0
# count = 1
# while count < 100:
#     if count % 2:  # count 对 2取余如果为 0 则该条件不成立，说明 count 为偶数，count 对 2取余如果不为 0 则该条件成立，说明 count 为奇数
#         sum += count  # 奇数做加法
#     else:
#         sum -= count  # 偶数做减法
#     count += 1
# print(sum)
#
# # 总结：
# #     在bool值中，0 None 空 为 False，其他都为 True
#
# # 6. 用户登录（三次机会重试）
# count = 0
# while True:
#     user = input('username:')
#     pwd = input('password:')
#     if user == 'admin' and pwd == '123':
#         print('登录成功.')
#         break
#     else:
#         print('用户名密码不正确，请重试。')
#         count += 1
#     if count == 3:
#         print('登录验证超过三次，登录失败.')
#         break

# '''x or y x 为非零 则返回 x， 否则返回 y'''
# print(1 or 2)   # 1
# print(3 or 2)   # 3
# print(0 or 2)   # 2
# print(0 or 100) # 100
#
# '''x and  x为True，则返回y '''
# print(1 and 2)  # 2
# print(0 and 2)  # 0

# print(2 or 1< 3)
# print(2 or 1< 3 and 2)

name = input('姓名：')
age = int(input('年龄：'))

print('我叫%s, 我的年龄：%d，我的学习进度3%%.' %(name, age))

# 执行结果：
# 姓名：hkey
# 年龄：20
# 我叫hkey, 我的年龄：20，我的学习进度3%.

