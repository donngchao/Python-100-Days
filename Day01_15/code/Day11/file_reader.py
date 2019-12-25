# encoding: utf-8
'''
@author: developer
@software: python
@file: file_reader.py
@time: 2019/12/24 23:23
@desc:
'''


# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())


# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# print(type(lines))
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(pi_string)
# print(len(pi_string))

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# print(pi_string[:52]+"...")
# print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")