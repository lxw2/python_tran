#-*- coding:utf-8 -*-
# @Time : 2020/1/9 15:21
# @File : python_06_listfun.py

list1 = list(range(1,10))
print(list1)
list2 = list(range(5,15))
print(list2)

#1.cmp(list1,list2) 比较两个列表元素
# import operator
# print(operator.cmp(list1,list2))


#2.len(list1)
print(len(list1))

#3.max()
print(max(list1))
#4.min()
print(min(list1))
#5.list()
print(list(list1))
#6.list.append()
list1.append("zhha") #python 3.x append 没有返回值,直接修改源 变量
# a = list(range(1,10,1))
print(list1)
#6.1 list.pop  从右到左进行弹栈
list1.pop()
print(list1)
#6.3 list.remove  从左到右第移除指定索引元素a
list1.remove(2)
print(list1)
#7.list.extend() 列表末尾添加
list1.extend([0,00,0])
print(list1)
#8.list.index()

# print(list1)

#10.list.insert() 在指定索引位置添加
list1.insert(0,'pear2')
print(list1)
#11.list.reverser()c//对
list1.reverse()
print(list1)
#12.list.sort()
list1.sort()
print(list1)