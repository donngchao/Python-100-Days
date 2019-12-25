# encoding: utf-8
'''
@author: developer
@software: python
@file: division2.py
@time: 2019/12/25 21:00
@desc:
'''


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

'''
Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 9
Second number: 0
Traceback (most recent call last):
  File "division2.py", line 20, in <module>
    answer = int(first_number) / int(second_number)
ZeroDivisionError: division by zero

'''

'''
Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 3
Second number: 0
You can't divide by 0!

First number: 3
Second number: 2
1.5

First number: 
'''