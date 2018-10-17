import unittest
import assertor


class TestAssertorMethods(unittest.TestCase):
    def test_match(self):
        self.assertEqual(assertor.assert_response('400', 'Star War', '400', 'Star War'), 'Passed')

    def test_not_match(self):
        self.assertEqual(assertor.assert_response('400', 'Star Treck', '401', 'Star War'), 'Failed')


if __name__ == '__main__':
    unittest.main()
