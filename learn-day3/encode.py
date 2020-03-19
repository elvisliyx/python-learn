#-*- coding:utf-8 -*-

import sys
print(sys.getdefaultencoding())

s = '你好'

print(s.encode())

s_gbk = s.encode('gbk')
print(s_gbk)

s_to_utf = s_gbk.decode('gbk').encode('utf-8')

print('utf-8',s_to_utf)


