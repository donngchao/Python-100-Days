"""
输入学生考试成绩计算平均分

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""

import os
import time


def main():
    str = 'Welcome to Sweety Coffe and please enjoy yourself      '
    while True:
        print(str)
        time.sleep(0.0001)
        str = str[1:] + str[0:1]  # slice test
        # for Windows use os.system('cls') instead
        os.system('cls')


if __name__ == '__main__':
    main()
