import unittest

class TestCipher(unittest.TestCase):

    def test_basic_uppercase_shift(self):
        self.assertEqual(caesar_cipher("A", 1), "B")

    def test_basic_uppercase_wrap_around(self):
        self.assertEqual(caesar_cipher("Z", 1), "A")

    def test_basic_uppercase_string(self):
        self.assertEqual(caesar_cipher("HELLO", 1), "IFMMP")

    def test_basic_lowercase_shift(self):
        self.assertEqual(caesar_cipher("a", 1), "b")

    def test_basic_lowercase_wrap_around(self):
        self.assertEqual(caesar_cipher("z", 1), "a")

    def test_basic_lowercase_string(self):
        self.assertEqual(caesar_cipher("hello", 1), "ifmmp")

    def test_mixed_string(self):
        self.assertEqual(caesar_cipher("Hello", 1), "Ifmmp")

    def test_mixed_string_with_wrap_around(self):
        self.assertEqual(caesar_cipher("Zebra", 2), "Bgdtc")

    

    #ABCDEFGHIJKLMNOPQRSTUVWXYZ