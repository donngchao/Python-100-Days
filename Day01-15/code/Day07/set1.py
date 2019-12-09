"""
定义和使用集合

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    apple = 'apple'
    set1 = {1, 2, 3, 3, 3, 2,apple}
    print(set1) #{1, 2, 3, 'apple'}
    set_test1 = {11,11,12,12,13,13,13}
    print("set_test1 is ",set_test1) #set_test1 is  {11, 12, 13}
    print('Length of set1 =', len(set1))
    print('Length of set_test1 =', len(set_test1)) #Length of set_test1 = 3
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set_test1.update([14,15])
    print("set_test1 is : ",set_test1) #set_test1 is :  {11, 12, 13, 14, 15}
    set_test1.add(100)
    print("set_test1 is now : ", set_test1) #set_test1 is now :  {100, 11, 12, 13, 14, 15}
    #set_test1.remove(1000)
    '''
        set_test1.remove(1000)
        KeyError: 1000
    '''
    set_test1.discard(15)
    print("set_test1 is now : ", set_test1) #set_test1 is now :  {100, 11, 12, 13, 14}
    set2.update([11, 12])
    print(set1)
    print(set2)
    set2.discard(5)
    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)
    # 遍历集合容器
    for elem in set2:
        print(elem ** 2, end=' ')
    print()
    # 将元组转换成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3)  #{1, 2, 3}
    print(set3.pop())
    print(set3)
    set_test1.pop() #{11, 12, 13, 14}
    '''
    pop:
     Remove and return an arbitrary set element.
     Raises KeyError if the set is empty.
    '''
    if 14 in set_test1:
        set_test1.remove(14)
    print(set_test1)  #{11, 12, 13}




if __name__ == '__main__':
    main()
