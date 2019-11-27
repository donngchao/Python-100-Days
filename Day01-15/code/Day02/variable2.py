"""
将input函数输入的数据保存在变量中并进行操作

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

"""
将input函数输入的数据保存在变量中并进行操作
使用float()函数将输入的字符串转换成浮点数
Version: 0.2
Author: developer
Date: 2019-11-27
"""

a = int(input('a = '))
b = int(input('b = '))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)#a ^ b
'''
a = 10
b = 3
13
7
30
3.3333333333333335
3
1
1000
'''

c = float(input('c : '))
d = float(input('d : '))
print(c + d)
print(c - d)
print(c * d)
print(c / d)
print(c // d)
print(c % d)
print(c ** d)

'''
c : 2
d : 5
7.0
-3.0
10.0
0.4
0.0
2.0
32.0
'''