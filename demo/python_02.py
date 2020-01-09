#-*- coding:utf-8 -*-
# @Time : 2020/1/7 19:11
# @File : python_02.py

#输入输出
#语法 ,<变量> = input()
#如果输入的类型出错
# a= int(input("请输入整数")) #ValueError: invalid literal for int() with base 10
# b = float(input("请输入一个浮点数"))

# a = input("please input your name :")
# print(a)
print("=======分割符")

#语法 2：print(<输出项列表>，sep=分隔符，end=结束符)
print("mon","thu","wed",sep=',', end=';')

print("========分割符")
age = 3
name = "Tom"
# 通过 string.format 将引入变量 :字符串通过{1},{2} 的形式来调用变量
print("{0} was {1} years old ".format(name,age))
#可以通过% 来代替 format 顺序依旧
print("%s was %d years old"%(name,age))
print(name +" was " + str(age) + " years old ")
# \n 换行
print("what.s your name \n tom")

print("helloworld")
print('helloworld')
print('''thisis1line thisis2line thisis3line!''')

print("=========分割符")
import numpy as np
#使用random
import random
x = random.random()
print(x)
x = random.randrange(90,100)
print(x)
# 产生0-1之间的符合均匀分布的随机数
x = np.random.random((3,2))
print(x)

# 产生1-10之间的8个数
print(np.random.randint(1,10,8))
# 产生正态分布的随机数 均值是0  方差是1
print (np.random.randn(2,4))
print(np.random.normal(0,1,size=(2,4))) #第一个参数标识均值,第二个标识的是方差

# 产生二项分布的随机数
print(np.random.binomial(10,0.5,size=(2,3))) #第一个参数是多少次实验 发生的概率是多少
#产生卡方分布的随机数
print(np.random.chisquare(2,(2,3))) #第一个参数标识的自由度
# gamma分布
print(np.random.gamma(2,4,100)) # 前两个参数的是自由度

# 创建多种随机主要是为了模拟生活中的测试数据