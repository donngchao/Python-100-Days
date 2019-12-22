# encoding: utf-8
'''
@author: developer
@software: python
@file: electric_car.py
@time: 2019/12/22 10:05
@desc:
'''


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

    def fill_gas_tank(self):
        """加油"""
        print("The car needs to fill gas tank to run.")


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


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
'''
2016 Tesla Model S
This car has a 70-kWh battery
This car can go approximately 240 miles on a full charge.
This car doesn't need a gas tank!
This car can go approximately 270 miles on a full charge.
'''