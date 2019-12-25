# encoding: utf-8
'''
@author: developer
@software: python
@file: word_count.py
@time: 2019/12/25 21:30
@desc:
'''


def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename, 'rb') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " do not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

#
# filename = 'alice.txt'
# count_words(filename)


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

'''
The file alice.txt has about 17842 words.
Sorry, the file siddhartha.txt do not exist.
The file moby_dick.txt has about 215829 words.
The file little_women.txt has about 189079 words.
'''