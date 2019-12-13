"""
用for循环实现1~100之间的偶数求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""


def addeven():
    sum = 0
    for x in range(2, 101, 2):
        sum += x
    print('the even number sumed to :',sum)
    return sum

def addforfun():
    result = 3
    for x in range(3, 20, 4):  #[3, 7, 11, 15, 19]
        result += x
    return result



addeven()
print(addforfun())
