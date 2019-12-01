"""
列表常用操作
- 列表连接
- 获取长度
- 遍历列表
- 列表切片
- 列表排序
- 列表反转
- 查找元素

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end=' ')  #  Grape Apple Strawberry Waxberry Pitaya Pear Mango

    print()
    # 列表切片
    fruits2 = fruits[1:4] # fruits has not changed
    print(fruits2) #['apple', 'strawberry', 'waxberry']
    # fruit3 = fruits  # 没有复制列表只创建了新的引用
    fruits3 = fruits[:] # slice a new variable
    print(fruits) #['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    print(fruits3) #['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    fruits3[1] = 'orange'

    print(fruits)  #['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    print(fruits3) #['grape', 'orange', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']

    fruits4 = fruits[-3:-1]
    print(fruits4)   #['pitaya', 'pear']
    fruits5 = fruits[::-1] #list has been reversed
    print(fruits5) #['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']



if __name__ == '__main__':
    main()
