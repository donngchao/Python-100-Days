# encoding: utf-8
'''
@author: developer
@software: python
@file: example10_6.py
@time: 2019/12/25 21:55
@desc:
'''


print("Please input two numbers to calculate the sum of them.")
first_num = input("Please input the first number:")
try:
    first_num = int(first_num)
except ValueError:
    print("You can not convert ", first_num, "into integer.")

second_num = input("Please input the second number:")
try:
    second_num = int(second_num)
except ValueError:
    print("You can not convert ", second_num, "into integer.")
else:
    result = first_num + second_num
    print("The sum of " + str(first_num) + " and " + str(second_num) + " is " + str(result))

'''
Please input two numbers to calculate the sum of them.
Please input the first number:9
Please input the second number:ppp
You can not convert  ppp into integer.
'''