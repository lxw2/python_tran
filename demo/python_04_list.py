#-*- coding:utf-8 -*-
# @Time : 2020/1/9 11:38
# @File : python_04_list.py

# 列表的特点

# 创建 :[]

# 访问 : 根据下表来访问

#切片:[start:end:step]

#增加列表元素:直接根据下标赋值

#删除列表: del 列表[下标]

#1.列表
list_1=[1,2,3,4,5,6,5]
print(list_1)
print(type(list_1))

# 创建方式2-使用range对象来创建list
list_2= list(range(1,10,2))
print(list_2)
print(type(list_2 ))

#创建方式3 使用tuple 创建list
list_3 = list((1,2,3,4,5))
print(list_3)

#创建方式4 :使用set创建list
list_4 = list({1,2,3,4,5,6})
print(list_4)

# 创建方式5: 使用字典来创建list
list_5 = list({"a":1,"b":2})
print(list_5)

#补充函数
print(len(list_2)) #返回长度
print(list_1*4) #重复4次
print(list_1+list_2) # 集合合并
print (4 not in list_1)  #判断
#切片操作
print (list_1)
print (list_1[-2])
print (list_1[::])
print (list_1[::2])   #从零开始每隔一个取
print (list_1[1::2])  #打印偶数
print (list_1[0:3])  #打印前三个
