# encoding: utf-8
'''
@author: developer
@software: python
@file: example9_13.py
@time: 2019/12/22 23:56
@desc:
'''

from collections import OrderedDict
table = OrderedDict()
table["python"] = "A programming language."
table["linux"] = "A operating system."
table["redis"] = "A cache database."
for word, meaning in table.items():
    print(word, "means", meaning)

'''
python means A programming language.
linux means A operating system.
redis means A cache database.
'''