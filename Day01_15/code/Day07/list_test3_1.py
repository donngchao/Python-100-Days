# encoding: utf-8
'''
@author: developer
@software: python
@file: list_test3_1.py
@time: 2019/12/5 22:34
@desc: list test
'''
names = ['Alice', 'Julie', 'Kim', 'Keler']
print("My first friend is  :"+names[0])
print("My second friend is :"+names[1])
print("My third friend is  :"+names[2])
print("My last friend is   :"+names[3])
print(type(names[0]))  # <class 'str'>

for name in names:
    message = ", How are you? My friend."
    print(name+message)

traffic_ways = ['car', 'motorcycle', 'bike', 'airplane']
for traffic_way in traffic_ways:
    print("I would like to own the "+traffic_way + ".")