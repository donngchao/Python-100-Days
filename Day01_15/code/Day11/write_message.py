# encoding: utf-8
'''
@author: developer
@software: python
@file: write_message.py
@time: 2019/12/25 20:32
@desc:
'''


filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

