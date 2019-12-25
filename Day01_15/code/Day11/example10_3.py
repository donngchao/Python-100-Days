# encoding: utf-8
'''
@author: developer
@software: python
@file: example10_3.py
@time: 2019/12/25 20:38
@desc:
'''


filename = 'guest.txt'
name = input("Please input your name:")
with open(filename, 'w') as fileobject:
    fileobject.write(name)

