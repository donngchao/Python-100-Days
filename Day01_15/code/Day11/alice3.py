# encoding: utf-8
'''
@author: developer
@software: python
@file: alice3.py
@time: 2019/12/25 21:25
@desc:
'''


filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file "+filename+"do not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file "+filename+" has about "+str(num_words)+" words.")

filename2 = 'sanguo.txt'
try:
    with open(filename2) as f_obj2:
        contents = f_obj2.read()
except FileNotFoundError:
    msg2 = "Sorry, the file "+filename2+"do not exist."
    print(msg2)
else:
    words = contents.split()
    num_words = len(words)
    print("The file"+filename2+" has about "+str(num_words)+" words.")
'''
The file alice.txt has about 17842 words.

'''