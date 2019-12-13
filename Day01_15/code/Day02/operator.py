"""
运算符的使用

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

a = 5
b = 10
c = 3
d = 4
e = 5
a += b # a = 15
a -= c # a = 12
a *= d # a = 48
a /= e # a = 9.6
print("a = ", a)#a =  9.6

flag1 = 3 > 2  #True
flag2 = 2 < 1  #False
flag3 = flag1 and flag2 #False
flag4 = flag1 or flag2  #True
flag5 = not flag1       #False
print("flag1 = ", flag1)#flag1 =  True
print("flag2 = ", flag2)#flag2 =  False
print("flag3 = ", flag3)#flag3 =  False
print("flag4 = ", flag4)#flag4 =  True
print("flag5 = ", flag5)#flag5 =  False
print(flag1 is True)    #True
print(flag2 is not False)#False
print(not flag4)        #False
print("1" is True)      #False

print(4 + 4)
print(3 + 5)
print(1 + 7)
print(2 * 4)
print(16 // 2)
print(18 -10)
'''
8
8
8
8
8
8
'''