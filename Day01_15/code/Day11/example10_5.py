# encoding: utf-8
'''
@author: developer
@software: python
@file: example10_5.py
@time: 2019/12/25 20:45
@desc:
'''

con = True
filename = "reason_of_programming.txt"
while con:
    reason = input("Please tell me why you like programming ? ")
    if reason != "I have no other reasons.":
        with open(filename, 'a') as fileObj:
            fileObj.write(reason+"\n")
    else:
        break
