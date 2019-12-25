# encoding: utf-8
'''
@author: developer
@software: python
@file: number_writer.py
@time: 2019/12/25 22:51
@desc:
'''


import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)