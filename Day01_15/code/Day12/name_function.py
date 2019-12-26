# encoding: utf-8
'''
@author: developer
@software: python
@file: name_function.py
@time: 2019/12/26 23:56
@desc:
'''


def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name"""
    full_name = first+' '+last
    return full_name.title()
