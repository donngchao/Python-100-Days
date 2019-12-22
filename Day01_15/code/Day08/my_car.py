# encoding: utf-8
'''
@author: developer
@software: python
@file: my_car.py
@time: 2019/12/22 15:05
@desc:
'''

from Day01_15.code.Day08.car import Car
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
