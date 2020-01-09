#-*- coding:utf-8 -*-
# @Time : 2020/1/9 14:44
# @File : python_05_zip_enumerate.py

#zip函数:用于将多个列表元素重新组合为元组,并返回这些元组的zip对象
a = zip([1,2,3],[9,7,6])
print(list(a))
a = zip([1,2,3,4],[9,7,6]) # 数量不同的列表进行zip
print(list(a))
list_1 = list(range(0,10))
list_2 = [1]*11
print(list(zip(list_1,list_2)))


#enumerate() 函数返回包含若干个下表和值的迭代对象
#返回的是一个枚举类型的对象

print(list(enumerate(list_2,start=1))) #生成一个带索引的集合
