# encoding: utf-8
'''
@author: developer
@software: python
@file: print_model_function.py
@time: 2019/12/16 23:43
@desc:
'''


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Pringting model: "+current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case','robot','dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models) # use [:] as a copy
show_completed_models(completed_models)
print(unprinted_designs)

