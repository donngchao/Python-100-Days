# encoding: utf-8
'''
@author: developer
@software: python
@file: delete_list_test5.py
@time: 2019/12/5 23:12
@desc:
'''
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me. ")
fruits = ['apple', 'orange', 'banana', 'banana']
print(fruits)
fruits.remove('banana') # remove() only remove the first one
print(fruits)

'''
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']

A Ducati is too expensive for me. 
['apple', 'orange', 'banana', 'banana']
['apple', 'orange', 'banana']
'''