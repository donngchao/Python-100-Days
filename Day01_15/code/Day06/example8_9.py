# encoding: utf-8
'''
@author: developer
@software: python
@file: example8_9.py
@time: 2019/12/16 23:56
@desc:
'''

magicians = ['david', 'john', 'liuqian']


def show_magicians(magicians):
    magicians_inside = make_great(magicians)
    for magician in magicians_inside:
        print("Show the magician: "+magician)


def make_great(magicians):
    new_magician = []
    for magician in magicians:
        new_magician.append("the Great "+magician.title())
    return new_magician


show_magicians(magicians)

print(make_great(magicians[:]))
print("***********")
print(magicians)
