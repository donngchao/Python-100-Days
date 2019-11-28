"""
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.1
Author: 骆昊
Date: 2018-02-28
"""

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))


'''
        7x + 6  (x > 5)
f(x) =  6x - 9    (-5 <= x <= 5)
        3x + 36  (x < -5)
'''

b = float(input("please input number b: "))
if b > 5:
    a = 7 * b + 6
elif b >= -5:
    a = 6 * b - 9
else:
    a = 3 * b + 36

print('f(%.2f) = %.2f'%(b,a))

'''
x = 9
f(9.00) = 22.00
please input number b: 9
f(9.00) = 69.00
'''