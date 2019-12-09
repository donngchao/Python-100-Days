"""
元组的定义和使用

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    # 定义元组
    t = ('developer', 27, True, '四川成都', 'eating',[1,2,3,4])
    print(t)
    # 获取元组中的元素
    print('t[0]=', t[0])
    print('t[1]=', t[1])
    print('t[2]=', t[2])
    print('t[3]=', t[3])
    print('t[4]=', t[4])
    print('t[5]=', t[5])

    '''
    IndexError: tuple index out of range
    '''

    # 遍历元组中的值
    for member in t:
        print('tuple member: --->', member)
    # 重新给元组赋值
    # t[0] = '王大锤'      # TypeError: 'tuple' object does not support item assignment
    # 变量t重新引用了新的元组 原来的元组被垃圾回收
    t = ('王大锤', 20, True, '云南昆明')
    print(t)  #('王大锤', 20, True, '云南昆明')
    # 元组和列表的转换
    person = list(t)  #change tuple to list
    print(person) #['王大锤', 20, True, '云南昆明']
    person[0] = '李小龙'
    person[1] = 25
    person[2] = False
    person[3] = '中国'
    print(person)  #['李小龙', 25, False, '中国']
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)  # change list to tuple
    print(fruits_tuple)  #('apple', 'banana', 'orange')
    print(fruits_tuple[1]) #banana
    #fruits_tuple[0] = 'pear'
    #TypeError: 'tuple' object does not support item assignment
    mood_tuple = ('lose','worry','unhappy')
    print(mood_tuple) #('lose', 'worry', 'unhappy')
    mood_list = list(mood_tuple)
    mood_list[2] = 'you should be happy'
    print(mood_list) #['lose', 'worry', 'you should be happy']


if __name__ == '__main__':
    main()