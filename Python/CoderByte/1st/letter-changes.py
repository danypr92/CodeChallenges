#!/usr/bin/python3

import unittest

import unittest

def LetterChanges(str):
    """Using the Python language, have the function LetterChanges(str)
    take the str parameter being passed and modify it using the
    following algorithm. Replace every letter in the string with
    the letter following it in the alphabet (ie. c becomes d, z
    becomes a). Then capitalize every vowel in this new string
    (a, e, i, o, u) and finally return this modified string."""
    new_str = ''
    for c in str:
        if c.isalpha():
            c = chr(ord(c) + 1)
            if c in ['a', 'e', 'i', 'o', 'u']: c = c.upper()
        new_str += c
    return new_str

class TestLetterChanges(unittest.TestCase):

    def test_1(self):
        self.assertEqual(LetterChanges("hello world"), "Ifmmp xpsmE")

    def test_2(self):
        self.assertEqual(LetterChanges("replace!*"), "sfqmbdf!*")

    def test_3(self):
        self.assertEqual(LetterChanges("beautiful^"), "cfbvUjgvm^")

    def test_4(self):
        self.assertEqual(LetterChanges("123456789ae"), "123456789bf")

    def test_5(self):
        self.assertEqual(LetterChanges("this long cake@&"), "UIjt mpOh dblf@&")

    def test_6(self):
        self.assertEqual(LetterChanges("a confusing /:sentence:/[ this is not!!!!!!!~"), "b dpOgvtjOh /:tfOUfOdf:/[ UIjt jt OpU!!!!!!!~")

if __name__ == '__main__':
    unittest.main()
