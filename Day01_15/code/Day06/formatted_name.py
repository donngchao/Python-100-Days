# encoding: utf-8
'''
@author: developer
@software: python
@file: formatted_name.py
@time: 2019/12/15 20:00
@desc:
'''


def get_formatted_name(first_name, last_name,middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)