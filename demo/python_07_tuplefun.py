#-*- coding:utf-8 -*-
# @Time : 2020/1/9 15:57
# @File : python_07_tuplefun.py

#元组的创建
tuple_1 =(1,2,3,4,4)
print(tuple_1)

#range对象创建元组

tuple_2 = tuple(range(1,5))
print(tuple_2)
print(type(tuple_2))

#list 转换 tuple
tuple_3 = tuple([1,2,3,4])
print(tuple_3)

#集合
tuple_4 = tuple({1,2,3,4})
print(tuple_4)
#通过字典从创建tuple
tuple_5  = tuple({"a":1,"b":2})
tuple_6  = tuple({"a":1,"b":2}.items())
tuple_7  = tuple({"a":1,"b":2}.values())
print(tuple_5)
print(tuple_6)
print(tuple_7)

#r如果元组中只有一个元组,能够作为元组 需要+,
t1 = (1)
t2 = (1,)
print(type(t1)) # 不加逗号的话 会改变类型
print(type(t2))

#访问方式
print(tuple_5[1])

print(4 in tuple_2)

#序列解包
v = 1,2,3
(a,b,c) = v
v = a,b,c
print(type(v))
print(a,b,c)
# print(a,b,c)


