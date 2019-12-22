# encoding: utf-8
'''
@author: developer
@software: python
@file: example9_14.py
@time: 2019/12/23 0:07
@desc:
'''

from random import randint


class Die():
    """定义一个骰子类"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        number = randint(1, self.sides)
        print("Roll the die of "+str(self.sides)+" sides with:"+str(number))


die_six = Die()
for time_of_roll in range(10):
    die_six.roll_die()

die_ten = Die(10)
for time_of_roll in range(10):
    die_ten.roll_die()

die_twenty = Die(20)
for time_of_twenty in range(20):
    die_twenty.roll_die()