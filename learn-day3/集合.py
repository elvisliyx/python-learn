# -*- coding:utf-8 -*-

list_1 = [1,2,3,4,5,6,7,9]
list_1 = set(list_1)
list_2 = set([0,1,4,5,6,66,88,11])
print(list_1,list_2)

#交集
print(list_1.intersection(list_2))
print(list_1 & list_2)


#并集
print(list_1.union(list_2))
print(list_1 | list_2)


#差集 in list_1 but not in list_2
print(list_1.difference(list_2))
print(list_1 - list_2)


#子集、父集
list_3 = set([2,4,6])
print(list_3.issubset(list_1))    #子集
print(list_1.issuperset(list_3))   #父集


#对称差集
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)


print("-------------------")
#没有交集就返回True，有交集就返回Fluse
list_4 = set([3,5,1])
print(list_3.isdisjoint(list_4))

#len()显示集合的长度
len(list_1)

#添加
list_1.app(999)
list_1.update(444,2222,6666)

#使用remove()可以删除一项
list_1.remove(2222)

#pop()随机删除一个并返回删除的值
list_1.pop()

#discard删除一项，没有的话返回None空，不会报错，remove会报错
list_1.discard()

