# encoding: utf-8
'''
@author: developer
@software: python
@file: example9_1.py
@time: 2019/12/21 0:03
@desc:
'''


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant's name is "+self.restaurant_name.title())
        print("This restaurant's cuisine_type is "+self.cuisine_type.title())

    def open_restaurant(self):
        print("This restaurant "+self.restaurant_name.title()+" with "+self.cuisine_type.title()+" is opening now !")


restaurant = Restaurant('cuihua', 'spicy')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

mrestaurant = Restaurant('micdonald', 'fastfood')
srestaurant = Restaurant('shanxian', 'snackfood')
mrestaurant.describe_restaurant()
srestaurant.describe_restaurant()

'''
cuihua
spicy
This restaurant's name is Cuihua
This restaurant's cuisine_type is Spicy
This restaurant Cuihua with Spicy is opening now !
This restaurant's name is Micdonald
This restaurant's cuisine_type is Fastfood
This restaurant's name is Shanxian
This restaurant's cuisine_type is Snackfood
'''
