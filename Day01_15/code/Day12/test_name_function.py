# encoding: utf-8
'''
@author: developer
@software: python
@file: test_name_function.py
@time: 2019/12/27 0:17
@desc:
'''

import unittest
from Day01_15.code.Day12.name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确处理Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()
'''

Ran 1 test in 0.002s

OK

Process finished with exit code 0
'''

'''

Error
Traceback (most recent call last):
  File "Programs\Python\Python37\lib\unittest\case.py", line 59, in testPartExecutor
    yield
  File "Programs\Python\Python37\lib\unittest\case.py", line 615, in run
    testMethod()
  File "test_name_function.py", line 18, in test_first_last_name
    formatted_name = get_formatted_name('janis', 'joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'



Ran 1 test in 0.004s

FAILED (errors=1)

Process finished with exit code 1

Assertion failed
'''