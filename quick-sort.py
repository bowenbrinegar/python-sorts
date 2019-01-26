import unittest


class tests(unittest.TestCase):
    def test1(self):
        test_case = [100,35,24,99,82,1,7,23,90,78,126,43,4,20,45,30]
        expected = [1,4,7,20,23,24,30,35,43,45,78,82,90,99,100,126]
        self.assertEqual(test_case, expected)

unittest.main()