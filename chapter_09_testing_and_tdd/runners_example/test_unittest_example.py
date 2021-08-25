import unittest
from tdd_example import parameter_tdd


class TestTDDExample(unittest.TestCase):

    def test_negative(self):
        self.assertEqual(parameter_tdd(-1), 0)

    def test_zero(self):
        self.assertEqual(parameter_tdd(0), 0)

    def test_five(self):
        self.assertEqual(parameter_tdd(5), 25)

    def test_seven(self):
        self.assertEqual(parameter_tdd(7), 0)

    def test_ten(self):
        self.assertEqual(parameter_tdd(10), 100)

    def test_eleven(self):
        self.assertEqual(parameter_tdd(11), 100)


if __name__ == '__main__':
    unittest.main()
