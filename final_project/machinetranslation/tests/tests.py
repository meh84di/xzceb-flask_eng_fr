import unittest
from translator import english_to_french, french_to_english

class test_translator(unittest.TestCase):

    ''' Function that test e2f translator '''
    def test_e2f(self):
        with self.assertRaises(TypeError):
            english_to_french()
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    ''' Function that test f2e translator '''
    def test_f2e(self):
        with self.assertRaises(TypeError):
            french_to_english()
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
