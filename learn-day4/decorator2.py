# -*- coding:utf-8 -*-

import time

def bar():
    time.sleep(2)
    print('in the bar')


def test1(func):
    print(func)
    func()

def test2(func1):
    start_time = time.time()
    func1()
    stop_time = time.time()
    print('the func run time is %s'%(stop_time-start_time))

# test1(bar)
# test2(bar)

def test3(func3):
    print(func3)
    return func3

# print(test3(bar))
# x = test3(bar)
# print(x)
# x()
bar = test3(bar)
bar()


