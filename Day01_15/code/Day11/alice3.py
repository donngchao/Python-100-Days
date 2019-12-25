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

'''
The file alice.txt has about 17842 words.

'''