"""
输入非负整数n计算n!

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
#calculate the factorial

def factorial1(n):
    result = 1
    # for x in range(1, n + 1):
    #     result *= x
    # print('%d! = %d' % (n, result))

    for y in range(n,0,-1):
        result *= y
    print('%d!=%d'%(n, result))
    return result

factorial1(3)
