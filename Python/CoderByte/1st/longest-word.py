#!/usr/bin/python3

import unittest

import unittest

def LongestWord(sen):
    """Using the Python language, have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. """
    longWord = ""
    for w in sen.split():
        for c in w:
            if not c.isalpha():
                w = w.replace(c, "")
        if len(w) > len(longWord):
            longWord = w
    return longWord

class TestLetterChanges(unittest.TestCase):

    def test_1(self):
        self.assertEqual(LongestWord("fun&!! time"), "time")

    def test_2(self):
        self.assertEqual(LongestWord("I love dogs"), "love")

if __name__ == '__main__':
    unittest.main()
