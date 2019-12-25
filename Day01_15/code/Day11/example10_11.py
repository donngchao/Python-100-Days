# encoding: utf-8
'''
@author: developer
@software: python
@file: example10_11.py
@time: 2019/12/25 23:44
@desc:
'''

import json
try:
    with open('favorite_number_test.json') as f_obj:
        num = json.load(f_obj)
    print("I know your favorite number! It's", num)
except FileNotFoundError:
    num = input("Please input your favorite number:")
    with open('favorite_number_test.json', 'a') as f_obj:
        json.dump(num, f_obj)

    '''
    I know your favorite number! It's 8

    '''