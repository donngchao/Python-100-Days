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

str5 = 'go!go!go!'
print(str5, "***", type(str5))
str6 = "python is a kind of programming language!"
print(str6, "***", type(str6))
'''
go!go!go! *** <class 'str'>
python is a kind of programming language! *** <class 'str'>
'''

str7 = 'I want to say " is allowed in python string'
print(str7)
# I want to say " is allowed in python string

str8 = "I'm tired after a the day job"
print(str8)
# I'm tired after a the day job

name_test = "central park"
print(name_test.title())
# Central Park
name_test2 = 'CeNtRal PaRk'
print(name_test2.title())
# Central Park
print(name_test.upper())
print(name_test.lower())
'''
CENTRAL PARK
central park
'''

first_name = "Jimmy"
last_name = "Jack"
full_name = first_name + " " + last_name
print(full_name)  # Jimmy Jack
print("Hello, "+full_name.title()+" !")
hello_message = "Hello, "+full_name.upper()+" !"
print(hello_message)

print("Python")
print("\tPython")

'''
Python
	Python
'''
print("Languages:\n\tPython\n\tGo\n\tRuby")
'''
Languages:
	Python
	Go
	Ruby
'''

hobby = 'playing games  '
print(hobby.rstrip()+'be happy')
#playing gamesbe happy

'''
>>> speak = 'English '
>>> speak
'English '
>>> speak.rstrip()
'English'
>>> speak
'English '
>>> speak = speak.rstrip()
>>> speak
'English'
>>> speak = ' English '
>>> speak.rstrip()
' English'
>>> speak.lstrip()
'English '
>>> speak.strip()
'English'
>>> speak
' English '
'''