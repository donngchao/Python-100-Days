# encoding: utf-8
'''
@author: developer
@software: python
@file: division.py
@time: 2019/12/25 20:56
@desc:
'''


try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

'''
Traceback (most recent call last):
  File "division.py", line 10, in <module>
    print(5/0)
ZeroDivisionError: division by zero
'''