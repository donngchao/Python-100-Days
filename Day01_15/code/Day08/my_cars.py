# encoding: utf-8
'''
@author: developer
@software: python
@file: my_cars.py
@time: 2019/12/22 15:34
@desc:
'''

from Day01_15.code.Day08.car import Car, ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
'''
2016 Volkswagen Beetle
2016 Tesla Roadster
'''