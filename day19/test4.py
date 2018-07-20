# -*- coding: utf-8 -*-
# Author: hkey
# def foo():
#     print('in the foo')
#     def bar():
#         print('in the bar')
#     bar()
# foo()

x = 0
def grandpa():
    def dad():
        x = 2
        def son():
            x =3
            print(x)
        son()
    dad()
grandpa()

# 执行结果：
# 3

# 上面嵌套函数执行顺序:
# (1) 当调用 grandpa() 返回 dad()
# (2) 当调用 dad() 返回 son()
# (3) 当调用 son() 赋值 x = 3，打印 x 的值 3
#
# 嵌套函数的执行，要求每一层级的函数都必须执行（调用），否则最外层不会执行最内层的函数
