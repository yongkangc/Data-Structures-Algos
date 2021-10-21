from fraction import Fraction


class MixedFraction(Fraction):
    def __init__(self, top, bot, whole=0):
        num = top + whole * bot
        self.whole = whole
        super().__init__(num, bot)

    @property
    def whole(self):
        return self._whole

    @whole.setter
    def whole(self, value):
        if isinstance(value, int):
            self._whole = value

    def get_three_numbers(self):
        if self.num > self.den:
            return self.num % self.den, self.den, self.num // self.den
        else:
            return self.num, self.den, self.whole

    def __str__(self):
        top, bot, whole = self.get_three_numbers()
        if whole > 0:
            return "{} {}/{}".format(whole, top, bot)
        else:
            return super().__str__()
