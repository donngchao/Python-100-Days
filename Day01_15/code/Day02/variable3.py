"""
格式化输出

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

"""
格式化输出

Version: 0.2
Author: developer
Date: 2019-11-27

使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串

"""

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
print('%d + %d + %d = %d' % (a,b,c,a+b+c))

num1 = input('num1 = ')
num2 = input('num2 = ')
#print(num1 * num2)

'''
Traceback (most recent call last):
  File "D:/Python-100-Days/Day01_15/code/Day02/variable3.py", line 36, in <module>
    print(num1 * num2)
TypeError: can't multiply sequence by non-int of type 'str'
'''
num1 = int(num1)
num2 = int(num2)
print('%d + %d = %d' % (num1, num2, num1 + num2))
print('%d - %d = %d' % (num1, num2, num1 - num2))
print('%d * %d = %d' % (num1, num2, num1 * num2))
print('%d / %d = %d ' % (num1,num2,num1 / num2))
print('%d // %d = %d '% (num1,num2,num1 // num2))

print('%d + %d = %d' % (num2,num1,num2 + num1))
print('%d - %d = %d '%(num2,num1,num2 - num1))
print('%d // %d = %d '%(num2,num1,num2 // num1))
print('%d %% %d = %d '% (num2,num1,num2 % num1))

"""
a = 3
b = 4
3 + 4 = 7
3 - 4 = -1
3 * 4 = 12
3 / 4 = 0.750000
3 // 4 = 0
3 % 4 = 3
3 ** 4 = 81
"""

'''
a = 3
b = 3
c = 3
3 + 3 = 6
3 - 3 = 0
3 * 3 = 9
3 / 3 = 1.000000
3 // 3 = 1
3 % 3 = 0
3 ** 3 = 27
3 + 3 + 3 = 9
num1 = 5
num2 = 6
5 + 6 = 11
5 - 6 = -1
5 * 6 = 30
5 / 6 = 0 
5 // 6 = 0 
6 + 5 = 11
6 - 5 = 1 
6 // 5 = 1 
6 % 5 = 1 
'''