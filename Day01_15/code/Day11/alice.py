# encoding: utf-8
'''
@author: developer
@software: python
@file: alice.py
@time: 2019/12/25 21:10
@desc:
'''


filename = 'alice.txt'
with open(filename) as f_obj:
    contents = f_obj.read()

'''
Traceback (most recent call last):
  File "alice.py", line 12, in <module>
    with open(filename) as f_obj:
FileNotFoundError: [Errno 2] No such file 
'''