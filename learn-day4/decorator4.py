# -*- coding:utf-8 -*-

import time

# def deco(func):
#     start_time = time.time()
#     return func    #func()
#     stop_time = time.time()
#     print('the func run tiem is %s' %(stop_time-start_time))

def timer(func):    #timer(test1)   func = test1
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)  #run test1
        stop_time = time.time()
        print('the func run time is %s' %(stop_time-start_time))
    return deco

@timer  #test1=timer(test1)
def test1():
    time.sleep(3)
    print('in the test1')

@timer  #test2=timer(test2)
def test2(name,age):
    # time.sleep(3)
    print('in the test2:',name,age)


# test1=deco(test1)
# test1()
# deco(test2)

# test1 = timer(test1)
test1()
test2('elvis',25)

