# encoding: utf-8
'''
@author: developer
@software: python
@file: my_electric_car.py
@time: 2019/12/22 15:17
@desc:
'''

from Day01_15.code.Day08.car import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
'''
2016 Tesla Model S
This car has a 70-kWh battery
This car can go approximately 240 miles on a full charge.
'''