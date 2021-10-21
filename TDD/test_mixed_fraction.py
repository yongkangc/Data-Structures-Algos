import unittest
from mixed_fraction import MixedFraction


class TestMixedFraction(unittest.TestCase):
    def setUp(self):
        self.mf1 = MixedFraction(1, 2)
        self.mf2 = MixedFraction(1, 3)

    def test_add(self):
        result = self.mf1 + self.mf2
        self.assertEqual(result.num, 5)
        self.assertEqual(result.den, 6)

    def test_str_output(self):
        self.assertEqual(str(self.mf1), "1/2")
        self.assertEqual(str(self.mf2), "1/3")


if __name__ == '__main__':
    unittest.main()
