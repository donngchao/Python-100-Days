# encoding: utf-8
'''
@author: developer
@software: python
@file: example9_3.py
@time: 2019/12/21 0:16
@desc:
'''


class User():
    def __init__(self, first_name, last_name, job):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job

    def describe_user(self):
        print("This user's first name is "+self.first_name.title())
        print("This user's last name is "+self.last_name.title())
        print("This user's job is "+self.job.title())

    def greet_user(self):
        print("How do you do, "+self.first_name.title()+" "+self.last_name.title())


mary = User("mary", "curie", "chemist")
einstein = User("albert", "einstein", "physicist")
zhangsan = User("shan", "zhang", "developer")
mary.describe_user()
einstein.describe_user()
zhangsan.describe_user()
mary.greet_user()
einstein.describe_user()
zhangsan.describe_user()

'''
This user's first name is Mary
This user's last name is Curie
This user's job is Chemist
This user's first name is Albert
This user's last name is Einstein
This user's job is Physicist
This user's first name is Shan
This user's last name is Zhang
This user's job is Developer
How do you do, Mary Curie
This user's first name is Albert
This user's last name is Einstein
This user's job is Physicist
This user's first name is Shan
This user's last name is Zhang
This user's job is Developer
'''