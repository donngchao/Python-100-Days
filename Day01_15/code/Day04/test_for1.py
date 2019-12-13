# encoding: utf-8
'''
@author: developer
@software: python
@file: test_for1.py
@time: 2019/12/13 21:28
@desc:
'''
import unittest

from Day01_15.code.Day04.for1 import *


class Testfor1(unittest.TestCase):
    """Test for1.py"""

    def test_sum1(self):
        """Test method sum1()"""
        self.assertEqual(5050, sum1())

    def test_sum2(self):
        """Test method sum2()"""
        self.assertEqual(0, sum2())

    def test_sum3(self):
        """Test method sum3()"""
        self.assertEqual(199970001, sum3())


if __name__ == '__main__':
    unittest.main()
