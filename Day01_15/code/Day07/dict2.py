"""
字典的常用操作

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    stu = {'name': '骆昊', 'age': 38, 'gender': True}
    print(stu)#{'name': '骆昊', 'age': 38, 'gender': True}
    print(stu.keys())#dict_keys(['name', 'age', 'gender'])
    print(stu.values())#dict_values(['骆昊', 38, True])
    print(stu.items())#dict_items([('name', '骆昊'), ('age', 38), ('gender', True)])
    for elem in stu.items():
        print(elem)
        print(elem[0], elem[1])
    #('name', '骆昊')
    #name 骆昊
    #('age', 38)
    #age 38
    #('gender', True)
    #gender True
    if 'age' in stu:
        stu['age'] = 20
    print(stu)
    stu.setdefault('score', 60)
    print('info with default score as 60:',stu)
    stu.setdefault('score', 100)
    """
            Insert key with a value of default if key is not in the dictionary.

            Return the value for key if key is in the dictionary, else default.
    """
    print('info with default score as 100:',stu)
    stu['score'] = 100
    print(stu)
    stu.setdefault('salary',1000)
    print('info with salary:',stu)
    '''
    info with salary: {'name': '骆昊', 'age': 20, 'gender': True, 'score': 100, 'salary': 1000}
    '''


if __name__ == '__main__':
    main()
