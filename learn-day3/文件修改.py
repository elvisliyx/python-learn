# -*- coding:utf-8 -*-

import sys

f = open('gequ',"r",encoding="utf-8")
f_new = open("gequ","w",encoding="utf-8")

for line in f:
    if "肆意的快乐等我享受" in line :
        line = line.replace("肆意的快乐等我享受","肆意的快乐等Elvis享受")
    f_new.write(line)
f.close()
f_new.close()

find_str = sys.argv[1]
replace_str = sys.argv[2]

for line in f:
    if find_str in line:
        line = line.replace(find_str,replace_str)






