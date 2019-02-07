#!/usr/bin/env python
# coding: utf-8

import unittest
from mymodule import MyModule


class TestMyModule(unittest.TestCase):

    def setUp(self):
        """Called before each test"""
        self.message = ('hohoho')

    def tearDown(self):
        """Called after each test (even if an error occurred)"""
        print('Clean on test')

    # Each methode need to start by test
    def test_format_message(self):
        """Test of format massge fucntion"""
        mm = MyModule()
        result = mm.format_message(self.message)

        self.assertEqual(result, self.message+"_format")


if __name__ == '__main__':
    unittest.main()
