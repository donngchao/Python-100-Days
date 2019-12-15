# encoding: utf-8
'''
@author: developer
@software: python
@file: printing_models.py
@time: 2019/12/15 22:27
@desc:
'''

unprinted_designs = ['iphone case','robot pendant','dodecahedrone']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Priting model:"+current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)