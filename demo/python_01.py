# -*- coding:utf-8 -*-
# @Time : 2020/1/7 17:14
# @File : python_01.py

# python 3.6 默认的字符编码是utf-8

s = "python 大数据"
print(s.encode())

# 通过import 来导入模块
import math

a = math.sin(0.5)
print(a)

# 只导入模型中的指定对象
from math import sin

b = sin(0.6)
print(b)

# import 模块之后可以通过as 给模块重命名
import numpy as np

a = np.array((1, 2, 3, 4))
print(a)

# python 的数据类型 Numeric & String
# 数据类型 总体:numeric,sequences,mappings,classes,instances,and exceptions
# Numeric Types : int(包含 boolean) , float , complex
a = 122
b = 221
c = 222
#id 可以获取对象的id标识
print(id(a))   #1946882320
print(id(122)) #1946882320
print(id(b))   #1946885488
print(id(c))   #1946885520
print(type(a)) #<class 'int'>

import sys

a=5
b=3

#返回一个复数
e = complex(a,b)
f = complex(float(a),float(b))

print("a is type",type(a))
print("b is type",type(b))
print("e is type",type(e))
print("f is type",type(f))

#real(实部)&imaginary(虚部）
print("e's real part is :" , e.real)
print("e's imaginary part is :" , e.imag)
print("=====分割符")
#加减乘除 算法
print("a:",a,"b:",b)
print("a+b",a+b)
print("a-b",a-b)
print("a*b",a*b)  #*乘法
print("a/b",a/b)  # /除法
print("a//b",a//b) #//整除
print("a**b",a**b) #**幂
print("a%b",a%b) #%取模
print("===分隔符")
#+=-= *=/=%= **=//=
print(a,b)
a += b
print(a,b)
a -= b
print(a,b)
a *= b
print(a,b)
a //= b
print(a,b)
a /= b
print(a,b)
a %= b
print(a,b)
print("=======分割符")

#& 按位与 | 按位或 ^按位异或 <<左移 >> 右移
a,b = 5,3
#0101 0011
print(5&3) #& 按位与
print(a|b)
print(a^b)
print(a<<2)
print(a>>2)
print(sys.int_info)
