# encoding: utf-8
'''
@author: developer
@software: python
@file: while4.py
@time: 2019/12/15 18:19
@desc:
'''
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
'''
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
'''