# -*- coding:utf-8 -*-

# #函数
# def func1():
#     "test"
#     print("in the funcl")
#     return 1
# #过程
# def func2():
#     'tests'
#     print('in the func2')
# x = func1()
# y = func2()
# print("func1 %s" %x)
# print("func2 %s" %y)

import time

def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('a.txt','a+') as f:
        f.write("%s in the test\n" %time_current)

def test1():
    print("test1 staring...")
    logger()

def test2():
    print("test2 staring...")
    logger()

def test3():
    print("test3 staring...")
    logger()

test1()
test2()
test3()

