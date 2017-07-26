#!/usr/bin/python3

import unittest

import unittest

def SimpleAdding(num):
    """Using the Python language, have the function SimpleAdding(num) add up all the numbers from 1 to num. For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10. For the test cases, the parameter num will be any number from 1 to 1000. """
    solution=0
    for n in range(num+1):
        solution+=n
    return solution

class TestLetterChanges(unittest.TestCase):

    def test_1(self):
        self.assertEqual(SimpleAdding(4), 10)

    def test_2(self):
        self.assertEqual(SimpleAdding(5), 15)

    def test_3(self):
        self.assertEqual(SimpleAdding(6), 21)

    def test_4(self):
        self.assertEqual(SimpleAdding(9), 45)

    def test_5(self):
        self.assertEqual(SimpleAdding(10), 55)

if __name__ == '__main__':
    unittest.main()
