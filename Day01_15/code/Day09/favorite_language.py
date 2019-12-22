# encoding: utf-8
'''
@author: developer
@software: python
@file: favorite_language.py
@time: 2019/12/22 23:50
@desc:
'''
from collections import OrderedDict
favorite_language = OrderedDict()
favorite_language['jen'] = 'python'
favorite_language['sarah'] = 'c'
favorite_language['edward'] = 'ruby'
favorite_language['phil'] = 'python'
for name, language in favorite_language.items():
    print(name.title()+"'s favorite language is "+language.title()+".")

'''
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.
'''