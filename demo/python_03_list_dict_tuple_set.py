#-*- coding:utf-8 -*-
# @Time : 2020/1/9 11:05
# @File : python_03_list_dict_tuple_set.py
# 1.列表的基础创建方式

list1 = [1,2,3,4,5]
print(list1)
print(type(list1))
    #1.1 列表的查询
print("第0个位置的元素是{0}".format(list1[0]))
print(list1[::]) # [start : end :step]
print(list1[::-1]) # 倒叙
print(list1[::2]) #输出奇数位上的数
print(list1[1::2]) # 输出偶数位上的数
print(list1[1:4]) # 指定的start到end 进行输出 包含start 不包含 end的位置的值

    #1.2 更改需求
list1[0] = 'a'
print(list1[::])
    # 删除
del list1[2]
print(list1[::])

#2.元组的基础创建方式

tuple = (1,2,3,4,5,6)
print(tuple)
print(type(tuple))
    #元组的查询 == 通过下表访问
print(tuple[0])
tuple = (1,2,3,4,["a","b"])
print(tuple[2])
print(tuple[3])
print(tuple[4])
    #元组元素的删除  不支持增删改   TypeError: 'tuple' object doesn't support item deletion
# del tuple[2]
# print(tuple[2])
    #元组的更改  不支持增删改  TypeError: 'tuple' object does not support item assignment
# tuple[2] = 2
# print(tuple[2])

# 3.字典的基础创建方式

zidian = {"a":1,"b":2,"c":3}
print(zidian)
print(type(zidian))
    #字典的查询
print(zidian.keys())   #返回字典里面的所有keys
print(zidian.values()) # 返回字典里面的所有值value
print(zidian.items())  #返回字典里面的所有key-value 键值对
print("========")
print(zidian["a"])
print(zidian["b"])
print(zidian["c"])

    #字典的删除
del zidian["a"]
# print(zidian["a"])

    #字典的清空
zidian.clear()
print(zidian.keys())


# 4.集合的基础创建放方式
#set 唯一性
list2={1,2,3,4,5,6,6,6,6}
print(list2)
print(type(list2))


# list :[] 列表
#  tuple : () 元组
#dict :{key:value } 字典
# set :{elment,elment} 不重复的集合