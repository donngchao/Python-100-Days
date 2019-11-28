"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):#每行显示对应行数的 *
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):#兜底要打的空格数和*数
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):# 空格的个数随着行数的增大而减小
        print(' ', end='')
    for _ in range(2 * i + 1):#  * 的个数是奇数
        print('*', end='')
    print()
