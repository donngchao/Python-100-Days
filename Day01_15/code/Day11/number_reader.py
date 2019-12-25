# encoding: utf-8
'''
@author: developer
@software: python
@file: number_reader.py
@time: 2019/12/25 22:57
@desc:
'''

import json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)