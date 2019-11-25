"""
用for循环实现1~100求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

sum = 0
for x in range(1, 101):
    sum += x
print('The sum of 1 to 100 is:',sum)

sum2 = 0
for y in range(-100,101):
    sum2 += y
print('The sum of -100 to 100 is:',sum2)