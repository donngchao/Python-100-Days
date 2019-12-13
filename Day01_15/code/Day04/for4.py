"""
输入一个正整数判断它是不是素数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
#  假如n是合数(not_prime)，必然存在非1的两个约数p1和p2，
# 其中p1<=sqrt(n)，p2>=sqrt(n)。由此我们可以改进上述方法优化循环次数。
# 素数指的是只能被1和自身整除的大于1的整数。
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

'''
请输入一个正整数: 3
3是素数
'''