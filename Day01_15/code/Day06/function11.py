def a_new_decorator(a_func):
    def wrapTheFunction():
        print("1")
        a_func()
        print("2")
    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")
    print("hold on!")


# a_function_requiring_decoration()
# outputs: I am doing some boring work before executing a_func()
#         I am the function which needs some decoration to remove my foul smell
#         I am doing some boring work after executing a_func()

# the @a_new_decorator is just a short way of saying:
b_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
b_function_requiring_decoration()
'''
1
1
I am the function which needs some decoration to remove my foul smell
hold on!
2
2
'''

# this function decorate 2 times