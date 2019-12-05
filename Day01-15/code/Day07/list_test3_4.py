# encoding: utf-8
'''
@author: developer
@software: python
@file: list_test3_4.py
@time: 2019/12/5 23:18
@desc: practice with list
'''
invite_people = ['Tom', 'Jerry', 'Doraemon']
cannot_come = invite_people.pop(0)
invite_people.append('Jack')
for people in invite_people:
    print("I want to invite "+people.title()+" to join me for the dinner.")

print(cannot_come+" can not come because of having some work to do.")

invite_people.insert(0, 'Lucy')
invite_people.insert(3, 'Kate')
invite_people.append('Mark')
print(invite_people)
for people in invite_people:
    print("I want to invite "+people.title()+" to join me for the dinner.")

last_one = invite_people.pop()
print("Sorry, "+last_one+" there is not enough food now.")
last_one = invite_people.pop()
print("Sorry, "+last_one+" there is not enough food now.")
last_one = invite_people.pop()
print("Sorry, "+last_one+" there is not enough food now.")
last_one = invite_people.pop()
print("Sorry, "+last_one+" there is not enough food now.")

for remain in invite_people:
    print("I will still invite "+remain.title()+" to join me for the dinner.")

del invite_people[1]
print(invite_people)
del invite_people[0]
print(invite_people)
print('End')
'''
I want to invite Jerry to join me for the dinner.
I want to invite Doraemon to join me for the dinner.
I want to invite Jack to join me for the dinner.
Tom can not come because of having some work to do.
['Lucy', 'Jerry', 'Doraemon', 'Kate', 'Jack', 'Mark']
I want to invite Lucy to join me for the dinner.
I want to invite Jerry to join me for the dinner.
I want to invite Doraemon to join me for the dinner.
I want to invite Kate to join me for the dinner.
I want to invite Jack to join me for the dinner.
I want to invite Mark to join me for the dinner.
Sorry, Mark there is not enough food now.
Sorry, Jack there is not enough food now.
Sorry, Kate there is not enough food now.
Sorry, Doraemon there is not enough food now.
I will still invite Lucy to join me for the dinner.
I will still invite Jerry to join me for the dinner.
['Lucy']
[]
End
'''