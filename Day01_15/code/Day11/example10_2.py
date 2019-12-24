# encoding: utf-8
'''
@author: developer
@software: python
@file: example10_2.py
@time: 2019/12/25 0:19
@desc:
'''

filename = 'learning_python.txt'
with open(filename) as readobject:
    string_list = readobject.readlines()

result = ''
for every_list in string_list:
    result += every_list.replace('Python', 'C')

print(result)

'''
In C you can build website.
In C you can do data analyse.
In C you can do AI.
In C you can do machine learning.
'''