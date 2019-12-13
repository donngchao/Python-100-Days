# encoding: utf-8
'''
@author: developer
@software: python
@file: test_for3.py
@time: 2019/12/13 22:08
@desc:
'''

from Day01_15.code.Day04.for3 import factorial1
import unittest

class Testfor3(unittest.TestCase):
    """Test for3.py"""

    def test_factorial1(self):
        """Test method factorial1()"""
        self.assertEqual(6, factorial1(3))




if __name__ == '__main__':
    unittest.main()
