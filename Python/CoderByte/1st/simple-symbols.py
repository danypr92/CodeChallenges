#!/usr/bin/python3

import unittest

import unittest

def SimpleSymbols(str):
    """Using the Python language, have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence by either returning the string true or false. The str parameter will be composed of + and = symbols with several letters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. The string will not be empty and will have at least one letter."""
    for i, c in enumerate(str):
        if c.isalpha() and (i-1< 0 or i+1>len(str) or str[i-1] != '+' or str[i+1] != '+'):
            return False
        elif c != "+" and c != "=" and not c.isalpha() and not c.isdigit():
            return False
    return True

class TestLetterChanges(unittest.TestCase):

    def test_1(self):
        self.assertTrue(SimpleSymbols("+d+=3=+s+"))

    def test_2(self):
        self.assertFalse(SimpleSymbols("f++d+"))

    def test_3(self):
        self.assertTrue(SimpleSymbols("+d+"))

    def test_4(self):
        self.assertTrue(SimpleSymbols("+z+z+==+a+"))

    def test_5(self):
        self.assertFalse(SimpleSymbols("==a+"))


if __name__ == '__main__':
    unittest.main()
