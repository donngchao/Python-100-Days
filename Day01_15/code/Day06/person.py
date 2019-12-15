# encoding: utf-8
'''
@author: developer
@software: python
@file: person.py
@time: 2019/12/15 20:54
@desc:
'''


def build_person(first_name,last_name,age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix',age=27)
print(musician)