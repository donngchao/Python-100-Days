# encoding: utf-8
'''
@author: developer
@software: python
@file: example10_1.py
@time: 2019/12/25 0:09
@desc:
'''


file_name = 'learning_python.txt'
with open(file_name) as file_object:
    result = file_object.read()

print(result)

with open(file_name) as file_object2:
    for line in file_object2:
        print(line.rstrip())

print("===================")

with open(file_name) as file_object3:
    line_list = file_object3.readlines()

line_string = ''
for items in line_list:
    line_string += items

print(line_string)

'''
In Python you can build website.
In Python you can do data analyse.
In Python you can do AI.
In Python you can do machine learning.

In Python you can build website.
In Python you can do data analyse.
In Python you can do AI.
In Python you can do machine learning.
===================
In Python you can build website.
In Python you can do data analyse.
In Python you can do AI.
In Python you can do machine learning.
'''