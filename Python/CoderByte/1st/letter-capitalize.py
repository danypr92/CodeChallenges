#!/usr/bin/python3

import unittest

import unittest

def LetterCapitalize(str):
    """Using the Python language, have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space."""
    sol_str = ""
    for w in str.split(" "):
        sol_str += w.capitalize()+" "
    return sol_str.strip()

class TestLetterChanges(unittest.TestCase):

    def test_1(self):
        self.assertEqual(LetterCapitalize("Argument goes here"), "Argument Goes Here")

if __name__ == '__main__':
    unittest.main()
