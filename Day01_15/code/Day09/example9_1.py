# encoding: utf-8
'''
@author: developer
@software: python
@file: example9_1.py
@time: 2019/12/21 0:03
@desc:
'''


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("This restaurant's name is " + self.restaurant_name.title())
        print("This restaurant's cuisine_type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print(
            "This restaurant " +
            self.restaurant_name.title() + " with " + self.cuisine_type.title() + " is opening now !")

    def update_number_served(self, people_served):
        if people_served > self.number_served:
            self.number_served = people_served
        else:
            print("The number of served should not be less than the people served originally.")

    def increment_number_served(self, increase):
        if increase > 0:
            self.number_served += increase
        else:
            print("The increase should be a positive number.")

    def get_number_served(self):
        print("Until now, " +
              str(self.number_served)+" people has been served in "+self.restaurant_name.title()+"restaurant !")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def show_icecream_flavor(self):
        for flavor in self.flavors:
            print("This icecream restaurant has flavor of:", flavor)



#
# restaurant = Restaurant('cuihua', 'spicy')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
# mrestaurant = Restaurant('micdonald', 'fastfood')
# srestaurant = Restaurant('shanxian', 'snackfood')
# mrestaurant.describe_restaurant()
# srestaurant.describe_restaurant()
#
# lamianrestaurant = Restaurant('lanzhoulamian', 'lamian')
# lamianrestaurant.open_restaurant()
# lamianrestaurant.update_number_served(10)
# lamianrestaurant.describe_restaurant()
# lamianrestaurant.get_number_served()
# lamianrestaurant.update_number_served(20)
# lamianrestaurant.increment_number_served(3)
# lamianrestaurant.get_number_served()
# icecream_restaurant = IceCreamStand('Häagen-Dazs', 'icecream')
# icecream_restaurant.open_restaurant()
# icecream_restaurant.describe_restaurant()
# icecream_restaurant.show_icecream_flavor()
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
This restaurant Lanzhoulamian with Lamian is opening now !
This restaurant's name is Lanzhoulamian
This restaurant's cuisine_type is Lamian
Until now, 10 people has been served in Lanzhoulamianrestaurant !
Until now, 23 people has been served in Lanzhoulamianrestaurant !
'''
