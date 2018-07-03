# -*- coding: utf-8 -*-
# Author: hkey

# def log(func):
#
#     def wrapper(*args, **kwargs):
#         print('call %s():' % func.__name__)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @log
# def now():
#     print('2018-07-03')
#
# now()



import time

def run_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print('app run time:', time.time() - start_time)
        return func
    return wrapper


@run_time
def test():
    time.sleep(1)
    print('app run finish.')

test()















