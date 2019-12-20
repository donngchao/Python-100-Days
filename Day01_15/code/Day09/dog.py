# encoding: utf-8
'''
@author: developer
@software: python
@file: dog.py
@time: 2019/12/20 23:04
@desc:
'''


class Dog():
    """模拟小狗"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+" rolled over!")


my_dog = Dog('willie', 6)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
print("Your dog's name is "+your_dog.name.title()+".")
print("Your dog is "+str(your_dog.age)+" years old.")
your_dog.sit()
'''
My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.
Willie rolled over!
Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is now sitting.
'''