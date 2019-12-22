# encoding: utf-8
'''
@author: developer
@software: python
@file: example9_11.py
@time: 2019/12/22 23:45
@desc:
'''

from Day01_15.code.Day09.example9_3 import Admin
admin = Admin('root', 'linux', 'dba')
admin.show_privileges()
'''
This user has the privilege of: can add post
This user has the privilege of: can delete post
This user has the privilege of: can ban user
'''