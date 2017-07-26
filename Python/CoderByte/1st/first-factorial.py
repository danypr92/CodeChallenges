#!/usr/bin/python3

import unittest

import unittest

def FirstFactorial(num):
    """Using the Python language, have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it (e.g. if num = 4, return (4 * 3 * 2 * 1)). For the test cases, the range will be between 1 and 18 and the input will always be an integer. """
    factorial = 1
    for n in range(num+1):
        if n != 0:
            factorial = factorial*n
    return factorial

class TestLetterChanges(unittest.TestCase):

    def test_1(self):
        self.assertEqual(FirstFactorial(4), 24)

    def test_2(self):
        self.assertEqual(FirstFactorial(8), 40320)

if __name__ == '__main__':
    unittest.main()
