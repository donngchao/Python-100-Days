# encoding: utf-8
'''
@author: developer
@software: python
@file: example10_4.py
@time: 2019/12/25 20:40
@desc:
'''


filename = "guest_book.txt"
while True:
    name = input("Please input your name here:")
    print("How are you recently ? ", name)
    with open(filename, 'a') as fileObj:
        fileObj.write(name+"has accessed.\n")
