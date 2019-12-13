# encoding: utf-8
'''
@author: developer
@software: python
@file: test_for2.py
@time: 2019/12/13 21:42
@desc:
'''

import unittest

from Day01_15.code.Day04.for2 import *


class Testfor2(unittest.TestCase):
    """Test for2.py"""

    def test_addeven(self):
        """Test method addeven()"""
        self.assertEqual(2550, addeven())

    def test_addforfun(self):
        """Test method addforfun()"""
        self.assertEqual(58, addforfun())


if __name__ == '__main__':
    unittest.main()
