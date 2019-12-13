# encoding: utf-8
'''
@author: developer
@software: python
@file: delete_list_test3.py
@time: 2019/12/5 22:58
@desc: delete_list_test using pop()
because list just likes a stack.
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)
print("The last motorcycle I owned was a "+poped_motorcycle.title()+".")
'''
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki
'''

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a "+first_owned.title()+".")
