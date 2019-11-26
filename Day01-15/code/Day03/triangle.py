"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
Author: 骆昊
Date: 2018-02-28
"""
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a <0 or b < 0 or c < 0:
    print('each length of the triangle should be positive number !\n')
elif a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))#海伦公式：S=√p(p-a)(p-b)(p-c)
    print('面积: %f' % (area))
else:
    print('不能构成三角形')
'''
a = 13
b = 14
c = 13
周长: 40.000000
面积: 76.681158
'''
