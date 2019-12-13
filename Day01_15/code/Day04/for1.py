"""
用for循环实现1~100求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

def sum1():
    sum = 0
    for x in range(1, 101):
        sum += x
    print('The sum of 1 to 100 is:', sum)
    return sum

def sum2():
    sum2 = 0
    for y in range(-100,101):
        sum2 += y
    print('The sum of -100 to 100 is:',sum2)
    return sum2

def sum3():
    sum3 = 0
    for z in range(1, 19999):
        sum3 += z
    print('The sum of 1...19999 is:',sum3)
    return sum3

sum1()
sum2()
sum3()