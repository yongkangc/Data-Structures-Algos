import unittest
from fraction import Fraction

# Documentation : https://docs.python.org/3/library/unittest.html#assert-methods


class TestFraction(unittest.TestCase):
    def setUp(self):
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(2, 3)
    # every method is a testcase

    def test_num_getter(self):
        """Test whether we can get the numerator"""
        self.assertEqual(self.f1.num, 1)
        self.assertEqual(self.f2.num, 2)

    def test_den_getter(self):
        """Test whether we can get the denominator"""
        self.assertEqual(self.f1.den, 2)
        self.assertEqual(self.f2.den, 3)

    def test_num_setter(self):
        self.f1.num = 3
        self.assertEqual(self.f1.num, 3)

        self.f2.num = "4"
        self.assertEqual(self.f2.num, 4)

    def test_den_setter(self):
        self.f2.den = "4"
        self.assertEqual(self.f2.den, 4)

    def test_denom_zero(self):
        self.f1.den = 0
        print(self.f1.den)
        self.assertEqual(self.f1.den, 1)

    def test_string_output(self):
        self.assertEqual(str(self.f1), "1/2")
        self.assertEqual(str(self.f2), "2/3")

    def test_plus(self):
        self.assertEqual(str(self.f1 + self.f2), str(Fraction(7, 6)))

    def test_eq(self):
        self.assertNotEqual(self.f1, self.f2)
        self.assertEqual(Fraction(2, 4), Fraction(1, 2))

    def test_subtract(self):
        self.assertEqual(str(self.f1 - self.f2), str(Fraction(-1, 6)))

    def test_multiply(self):
        self.assertEqual(str(self.f1 * self.f2), str(Fraction(1, 3)))

    def test_equal(self):
        self.assertEqual(Fraction(1, 2), Fraction(2, 4))

    def test_less_than(self):
        self.assertEqual(Fraction(1, 10) < Fraction(2, 4), True)
        self.assertEqual(Fraction(1, 2) < Fraction(1, 4), False)

    def test_lessthan_equals(self):
        self.assertEqual(Fraction(1, 10) <= Fraction(2, 4), True)
        self.assertEqual(Fraction(1, 10) <= Fraction(1, 10), True)


if __name__ == '__main__':  # am i running this file as a main programe?
    unittest.main(verbosity=4)  # run all tests
