# -*- coding:utf-8 -*-

f = open("gequ",encoding="utf-8",)
# data = f.read()
# print(data)



# f = open("gequ",'w',encoding="utf-8",)
# f.write("我不爱北京")

# f = open("gequ",'a',encoding="utf-8",)
# f.write("我不爱北京")

print(f.readline())

for i in range(5):
    print(f.readline())

for line in f.readlines():
    print(line.strip())

for index,line in enumerate(f.readlines()):
    if index == 9:
        print("-----------分割线----------")
        continue
    print(line.strip())


count = 0
for line in f:
    if count == 9:
        print('-----fengexian---------')
        count += 1
        continue
    print(line)
    count += 1

#打印文件光标的位置（按字符来计数）
f.tell()

#时光标回到指定位置
f.seek()

#打印文件的编码
f.encoding

#返回文件在系统里的编号
f.fileno()

#文件是不是一个终端
f.isatty()

#文件是否可读，可写
f.readable()
f.writable()

#强制刷新，把内存的内容写到硬盘上
f.flush()

#不写就是清空目录，从开头数10个字符然后截断
f.truncate(10)



f.close()