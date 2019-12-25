# encoding: utf-8
'''
@author: developer
@software: python
@file: greet_user.py
@time: 2019/12/25 23:04
@desc:
'''

import json
filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, "+username+"!")