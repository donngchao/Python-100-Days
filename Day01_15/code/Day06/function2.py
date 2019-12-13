"""
函数的定义和使用 - 求最大公约数和最小公倍数

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1


def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(15, 27))
print(lcm(15, 27))


def maxnum(x,y):
    if x > y:
        return x
    else:
        return y


print(maxnum(10, 100))

'''
3
135
100
'''