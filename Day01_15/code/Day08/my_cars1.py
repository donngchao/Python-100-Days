# encoding: utf-8
'''
@author: developer
@software: python
@file: my_cars1.py
@time: 2019/12/22 23:21
@desc:
'''

import Day01_15.code.Day08.car
my_beetle = Day01_15.code.Day08.car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = Day01_15.code.Day08.car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
'''
2016 Volkswagen Beetle
2016 Tesla Roadster
'''