"""
赋值运算符和复合赋值运算符

Version: 0.2
Author: developer
2019-11-27
"""

a = 10
b = 3
a += b # 相当于：a = a + b, a = 13
a *= a + 2 # 相当于：a = a * (a + 2) , 13 * 15
print(a) # 想想这里会输出什么-->195

c = 12
d = 9
c -= d
print(c) #3
c *= c + 9 # 相当于：c = c * (c + 9), 3 * 12
print(c) #36