"""
字符串常用操作

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

str1 = 'hello, world!'
print('字符串的长度是:', len(str1)) #13
print('单词首字母大写: ', str1.title()) #单词首字母大写:  Hello, World!
print('字符串变大写: ', str1.upper()) #字符串变大写:  HELLO, WORLD!
# str1 = str1.upper()
print('字符串是不是大写: ', str1.isupper())#  字符串是不是大写:  False

print('字符串是不是以hello开头: ', str1.startswith('hello')) # 字符串是不是以hello开头:  True
print('字符串是不是以hello结尾: ', str1.endswith('hello'))#字符串是不是以hello结尾:  False
print('字符串是不是以感叹号开头: ', str1.startswith('!'))#字符串是不是以感叹号开头:  False
print('字符串是不是一感叹号结尾: ', str1.endswith('!'))#字符串是不是一感叹号结尾:  True

str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)

str4 = 'try your best to swim in the pool.'
print(str4.title())
print(str4.upper())
print(str4.startswith('try'))
print(str4.endswith('pool.'))
print(str4.isupper())
'''
Try Your Best To Swim In The Pool.
TRY YOUR BEST TO SWIM IN THE POOL.
True
True
False
'''