"""
定义和使用矩形类

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""


class Rect(object):
    """矩形类"""

    def __init__(self, width=0, height=0):
        """初始化方法"""
        self.__width = width
        self.__height = height

    def perimeter(self):
        """计算周长"""
        return (self.__width + self.__height) * 2

    def area(self):
        """计算面积"""
        return self.__width * self.__height

    def __str__(self):
        """矩形对象的字符串表达式"""
        return '矩形[width : %.2f,height: %.2f]' % (self.__width, self.__height)

    def __del__(self):
        """析构器"""
        print('销毁矩形对象', self.__str__())
        print('garbage has been collected, do not worry...')


if __name__ == '__main__':
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())
    rect2 = Rect(3.5, 4.5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())
    rect3 = Rect(10, 10)
    print(rect3.__str__())
    print(rect3.perimeter())
    print(rect3.area())


'''
与 __init__() 方法对应的是 __del__() 方法，__init__() 方法用于初始化 Python 对象，
而 __del__() 则用于销毁 Python 对象，
即在任何 Python 对象将要被系统回收之时，系统都会自动调用该对象的 __del__() 方法。

当程序不再需要一个 Python 对象时，系统必须把该对象所占用的内存空间释放出来，
这个过程被称为垃圾回收（GC，Garbage Collector），
Python 会自动回收所有对象所占用的内存空间，因此开发者无须关心对象垃圾回收的过程。
'''

'''
矩形[width : 0.00,height: 0.00]
0
0
矩形[width : 3.50,height: 4.50]
16.0
15.75
矩形[width : 10.00,height: 10.00]
40
100
销毁矩形对象 矩形[width : 0.00,height: 0.00]
garbage has been collected, do not worry...
销毁矩形对象 矩形[width : 3.50,height: 4.50]
garbage has been collected, do not worry...
销毁矩形对象 矩形[width : 10.00,height: 10.00]
garbage has been collected, do not worry...
'''