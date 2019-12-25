# encoding: utf-8
'''
@author: developer
@software: python
@file: example10_10.py
@time: 2019/12/25 22:45
@desc:
'''


file_name = 'little_women.txt'
try:
    with open(file_name) as fileObj:
        result = fileObj.read()
except FileNotFoundError:
    pass

print(result.lower().count('she'))
"""统计she在文本中出现的次数"""
'''
2653
'''