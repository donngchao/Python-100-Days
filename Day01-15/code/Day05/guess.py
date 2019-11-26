"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if isinstance(number,int) and number > 0:
        print("Right! You input correct format of value")
    else:
        print("Wrong! You input the wrong format of value")
        break
    if number < answer:
        print('大一点')
        print('请输入大一点的数字再猜吧 ! ')
    elif number > answer:
        print('小一点')
        print('请输入小一点的数字再猜吧 ! ')
    else:
        print('恭喜你猜对了!')
        break

print('你总共猜了%d次' % counter)

if counter > 7:
    print('你的智商余额明显不足')

'''
请输入: 80
小一点
请输入: 40
小一点
请输入: 20
大一点
请输入: 30
大一点
请输入: 35
小一点
请输入: 33
大一点
请输入: 34
恭喜你猜对了!
你总共猜了7次
'''

'''    
number = int(input('请输入: '))
ValueError: invalid literal for int() with base 10: ''
'''