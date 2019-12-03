"""
函数的定义和使用 - 计算组合数C(7,3)

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""
import math

"""
C(n,m)=n!/((n-m)!*m!)（m≤n）
"""
# 将求阶乘的功能封装成一个函数
def factorial(n):
    if n == 0:
        result = 1
        return result
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


print(factorial(7) // factorial(3) // factorial(4))

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))

def square_root(n):
    return math.sqrt(n)

print(square_root(2))


def keep_happy():
    return  'you should be happy today.'

print(keep_happy())
'''
35
1
1
2
6
1.4142135623730951
you should be happy today.
'''