#-*- coding:utf-8 -*-
# @Time : 2020/1/9 16:09
# @File : python_08_dict.py

#字典:key+ value{}

#1.创建方式
dict1 = {1:'a',2:'b'}
print(dict)

#通过zip函数 创建dict
dict2 = dict(zip([1,2,3],['a','b','c']))
print(dict2)

#直接给定key value
dict3 = dict(name="zhansan",age="12")
print(dict3)

#需求 电话簿: 姓名+ 电话
dict4 = {"zhansan": 188,"lisi":137}
print(dict4)
#更改电话簿
dict4["zhansan"] = 111
print(dict4)

#删除字典
# dict4.clear() #清空
# print(dict4)
# del dict4
# print(dict4)

#使用update函数更新
dict4.update({"lisi":1233})  # 更新某个键
print(dict4)

a ="a"
dict_5 ={"a" : 1,"b ": 2}
# dict_5 ={["a"] : 1,"b ": 2}  //列表是可变的 不可以
dict_5 ={a: 1,"b ": 2}

print(dict_5["a"])

print(dict_5)
