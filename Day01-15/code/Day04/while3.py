"""
用while循环实现1~100之间的奇数求和

Version: 0.1
Author: tester
Date: 2019-11-26
"""
sum,num = 0,1
while num <= 100:
    sum += num
    num += 2

print("1到100的奇数之和为：",sum)
#1到100的奇数之和为： 2500