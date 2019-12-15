# encoding: utf-8
'''
@author: developer
@software: python
@file: example7_8.py
@time: 2019/12/15 18:31
@desc:
'''
sandwich_orders = ["butter","pastrami", "mayo", "pastrami","mustard","pastrami", "ketchup", "pesto"]
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("Pastrami has sold out.")

finished_sandwiches = []
while sandwich_orders:
    finish_sandwich = sandwich_orders.pop()
    print("I made your ",finish_sandwich,' sandwich')
    finished_sandwiches.append(finish_sandwich)

for sandwich in finished_sandwiches:
    print("I have successfully made ", sandwich, " flavored sandwich.")