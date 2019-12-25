# encoding: utf-8
'''
@author: developer
@software: python
@file: example10_8.py
@time: 2019/12/25 22:16
@desc:
'''

filename1 = 'cats.txt'
filename2 = 'dogs.txt'
files = [filename1, filename2]
for file in files:
    try:
        with open(file) as fileObj:
            print(fileObj.read())
    except FileNotFoundError:
        print("The file", file, "does not exist.")

'''
The file cats.txt does not exist.
The file dogs.txt does not exist.
'''