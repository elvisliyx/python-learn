# -*- coding:utf-8 -*-

def foo():
    print('in the foo')
    def bar():
        print('in the bar')
    bar()

foo()

