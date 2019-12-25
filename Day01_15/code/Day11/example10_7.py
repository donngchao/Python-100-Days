# encoding: utf-8
'''
@author: developer
@software: python
@file: example10_7.py
@time: 2019/12/25 22:07
@desc:
'''

while True:
    print("Please input two numbers to calculate the sum of them.")
    first_num = input("Please input the first number:")
    second_num = input("Please input the second number:")
    if first_num == 'quit' or second_num == 'quit':
        break
    else:
        try:
            first_num = int(first_num)
            second_num = int(second_num)
        except ValueError:
            print("You can not convert non-numerical values into integer.")
        else:
            result = first_num + second_num
            print("The sum of " + str(first_num) + " and " + str(second_num) + " is " + str(result))

'''
Please input two numbers to calculate the sum of them.
Please input the first number:kk
Please input the second number:9
You can not convert non-numerical values into integer.
Please input two numbers to calculate the sum of them.
Please input the first number:99
Please input the second number:kk
You can not convert non-numerical values into integer.
Please input two numbers to calculate the sum of them.
Please input the first number:9
Please input the second number:9
The sum of 9 and 9 is 18
Please input two numbers to calculate the sum of them.
Please input the first number:quit
Please input the second number:9
'''
