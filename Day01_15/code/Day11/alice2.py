# encoding: utf-8
'''
@author: developer
@software: python
@file: alice2.py
@time: 2019/12/25 21:12
@desc:
'''


filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

'''
Sorry, the file alice.txt does not exist.
'''