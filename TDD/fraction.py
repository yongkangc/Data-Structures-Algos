import logging


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    @property
    def num(self):
        return self._numattr

    @num.setter
    def num(self, value):
        self._numattr = int(value)

    @property
    def den(self):
        return self._denattr

    @den.setter
    def den(self, value):
        # ask about property and how it influences the attribute
        if value == 0:
            self._denattr = 1
        else:
            self._denattr = int(value)

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den).simplify()

    def simplify(self):
        common = gcd(self.num, self.den)
        num = self.num // common
        den = self.den // common
        return Fraction(num, den)

    def __eq__(self, other):
        left = self.simplify()
        right = other.simplify()
        return left.num == right.num and left.den == right.den

    def __sub__(self, other):
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den

        return Fraction(num, den).simplify()

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den).simplify()

    def __eq__(self, other):
        left = self.simplify()
        right = other.simplify()
        return left.num == right.num and left.den == right.den

    def __lt__(self, other):
        if self.num * other.den - other.num * self.den < 0:
            return True
        else:
            return False

    def __le__(self, other):
        if self.num * other.den - other.num * self.den <= 0:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.num * other.den - other.num * self.den > 0:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.num * other.den - other.num * self.den >= 0:
            return True
        else:
            return False

        # def gcd(a, b):
        #     """Returns Greatest Common Divisor of a and b"""
        #     while b:
        #         a, b = b, a % b
        #     return a


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
