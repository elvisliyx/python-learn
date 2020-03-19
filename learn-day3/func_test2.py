# -*- coding:utf-8 -*-


# def test1():
#     print('in the test1')
#     return 0
#
# test1()

def test(x,y):
    print(x)
    print(y)

test(1,2)   #与形参一一对应
test(x=4,y=1)   #与形参顺序无关



def test(args,**kwargs):
    print('fdasjlg')

test(1,3,35)

