# encoding: utf-8
'''
@author: developer
@software: python
@file: car.py
@time: 2019/12/21 23:09
@desc:
'''

"""一个用于表示汽车的类"""


class Car():
    """模拟汽车"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make.title()+' '+self.model.title()
        return long_name

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer !")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You not roll back an odometer")

class Battery():
    """模拟电动汽车电瓶"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            gorange = 240
        elif self.battery_size == 85:
            gorange = 270

        message = "This car can go approximately "+str(gorange)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

    # def describe_battery(self):
    #     """打印一条描述电瓶容量的消息"""
    #     print("This car has a "+str(self.battery_size)+"-kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.update_odometer(-19)
#
# my_new_car.read_odometer()
# '''
# 2016 Audi A4
# You can't roll back an odometer !
# This car has 23 miles on it.
# '''
#
# my_used_car = Car('sabaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
#
# his_car = Car('kia', 'v1', 2014)
# print(his_car.get_descriptive_name())
# his_car.update_odometer(1000000)
# his_car.read_odometer()
'''
2016 Audi A4
You can't roll back an odometer !
This car has 23 miles on it.
2013 Sabaru Outback
This car has 23500 miles on it.
This car has 23600 miles on it.
2014 Kia V1
This car has 1000000 miles on it.
'''