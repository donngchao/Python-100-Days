# encoding: utf-8
'''
@author: developer
@software: python
@file: example7_10.py
@time: 2019/12/15 18:40
@desc:
'''
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("If you could visit one place in the world, where would you go?")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n---Poll Results ---")
for name,response in responses.items():
    print(name+" would like to visit "+response+".")

    '''
    What is your name?mike
If you could visit one place in the world, where would you go?hawiii
Would you like to let another person respond?(yes/no)yes

What is your name?jack
If you could visit one place in the world, where would you go?losangeles
Would you like to let another person respond?(yes/no)no

---Poll Results ---
mike would like to visit hawiii.
jack would like to visit losangeles.

Process finished with exit code 0
    '''
