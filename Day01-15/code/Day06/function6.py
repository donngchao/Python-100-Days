"""
作用域问题

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""
'''
在Python程序中创建、改变、查找变量名时，都是在一个保存变量名的空间中进行，我们称之为命名空间，也被称之为作用域。
python的作用域是静态的，
在源代码中变量名被赋值的位置决定了该变量能被访问的范围。即Python变量的作用域由变量所在源代码中的位置决定。
'''

# 局部作用域
def foo1():
    a = 5


foo1()
#print(a)  # NameError
'''
    print(a)  # NameError
NameError: name 'a' is not defined
'''

# 全局作用域
b = 10


def foo2():#这里只是定义函数
    print(b)


foo2()#10,这里调用函数


def foo3():
    b = 100     # 局部变量
    print(b)


foo3()#100
print(b)#10，打印全局作用域的值


def foo4():
    global b
    b = 200     # 全局变量
    print(b)


foo4()#200
print(b)#200

if True:
    variable = 100
    print (variable) #100
print ("******")
print (variable)#100

'''
在if-elif-else、for-else、while、try-except\try-finally等关键字的语句块中并不会产成作用域
'''