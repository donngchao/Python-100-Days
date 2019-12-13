"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
'''
普通闰年:公历年份是4的倍数的，且不是100的倍数，为闰年。（如2004年就是闰年）；
世纪闰年:公历年份是整百数的，必须是400的倍数才是闰年（如1900年不是世纪闰年，2000年是世纪闰年）
'''
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)
if is_leap:
    print("This year is leap year : %d " %(year))

'''
请输入年份: 2008
True
This year is leap year : 2008 
'''