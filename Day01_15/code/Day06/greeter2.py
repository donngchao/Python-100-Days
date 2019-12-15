# encoding: utf-8
'''
@author: developer
@software: python
@file: greeter2.py
@time: 2019/12/15 21:00
@desc:
'''


def get_formatted_name(first_name,last_name):
    """返回简洁的姓名"""
    full_name = first_name+' '+last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, "+formatted_name+"!")