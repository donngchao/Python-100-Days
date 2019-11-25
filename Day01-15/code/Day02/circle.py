"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""
import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)

length = float(input('请输入长方形的长: '))
witdth = float(input('请输入长方形的宽: '))
perimeter2 = length * witdth
area2 = length * witdth
print('周长: %.2f' % perimeter2)
print('面积:%.2f' % area2)

'''
请输入圆的半径: 3
周长: 18.85
面积: 28.27
请输入长方形的长: 11
请输入长方形的宽: 11
周长: 121.00
面积:121.00
'''
