# encoding: utf-8
'''
@author: developer
@software: python
@file: names.py
@time: 2019/12/26 23:59
@desc:
'''


from Day01_15.code.Day12.name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\n Please give me a first name:")
    if first == 'q':
        break
    last = input("Please give me a last name:")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: "+formatted_name+".")