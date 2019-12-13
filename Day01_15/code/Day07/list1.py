"""
定义和使用列表
- 用下标访问元素
- 添加元素
- 删除元素

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    fruits = ['grape', '@pple', 'strawberry', 'waxberry']
    print(fruits)
    # 通过下标访问元素
    print(fruits[0])
    print(fruits[1])
    print(fruits[-1])
    print(fruits[-2])
    print(fruits[-1:-3:-1])  #['waxberry', 'strawberry']
    #print(fruits[-5]) # IndexError
    '''
        print(fruits[-5]) # IndexError
    IndexError: list index out of range
    '''
    # print(fruits[4])  # IndexError
    fruits[1] = 'apple' #直接修改列表元素
    print(fruits)  #['grape', 'apple', 'strawberry', 'waxberry']
    # 添加元素
    fruits.append('pitaya')  #['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
    print(fruits)
    fruits.insert(0, 'banana')
    print(fruits)   # ['banana', 'grape', 'apple', 'strawberry', 'waxberry', 'pitaya']

    # 删除元素
    del fruits[1]
    print(fruits)   #   ['banana', 'apple', 'strawberry', 'waxberry', 'pitaya']
    fruits.pop()
    print(fruits)  #  ['banana', 'apple', 'strawberry', 'waxberry']
    fruits.pop(0)
    print(fruits)  # ['apple', 'strawberry', 'waxberry']
    fruits.remove('apple')
    print(fruits)  #  ['strawberry', 'waxberry']



if __name__ == '__main__':
    main()
