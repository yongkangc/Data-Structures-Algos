import operator
from stack_q import Dequeue, Queue, Stack


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


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


class EvaluatePostfix:

    def __init__(self):
        self.expression = Queue()
        self.stack = Stack()
        self.ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,  # use operator.div for Python 2
            '%': operator.mod,
            '^': operator.xor}
        self.operands = "0123456789"

    def input(self, item):
        self.expression.enqueue(item)

    def evaluate(self):
        while self.expression.size != 0:
            item = self.expression.dequeue()
            print(item)

            if item in self.operands:
                self.stack.push(item)

            elif item in self.ops:
                op1 = int(self.stack.pop())
                op2 = int(self.stack.pop())
                print(op1, op2)

                product = self.ops[item](op2, op1)
                self.stack.push(product)

        test = self.stack.pop()
#         print(test,type(test))
        return test


class EvaluateFraction:

    operands = "0123456789"
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,  # use operator.div for Python 2
        '%': operator.mod,
        '^': operator.xor}

    def __init__(self):
        self.expression = Dequeue()
        self.stack = Dequeue()

    def input(self, item):
        """ Enqueues items"""
        if item in self.ops:
            self.expression.add_rear(item)
        else:
            self.expression.add_rear(self.get_fraction(item))
        print(f"peek front {self.expression.peek_front()}")
        print(f"peek back {self.expression.peek_rear()}")

    def evaluate(self):
        while self.expression.size != 0:
            item = self.expression.remove_front()
            print(item)

            if type(item) == Fraction:
                self.stack.add_front(item)

            elif item in self.ops:
                op1 = self.stack.remove_front()
                op2 = self.stack.remove_front()
                print(op1, op2)
                product = self.ops[item](op2, op1)
                self.stack.add_front(product)

        res = self.stack.remove_front()
        return res

    def get_fraction(self, inp):
        """Takes in inp string and returns Fraction object"""
        num, den = inp.split('/')
        return Fraction(int(num), int(den))


class EvaluateMixedFraction(EvaluateFraction):
    def get_fraction(self, inp):
        if len(inp.split(' ')) > 1:
            whole, frac = inp.split(' ')
            num, den = frac.split('/')
        else:
            whole = 0
            num, den = inp.split('/')
        return MixedFraction(int(num), int(den), int(whole))

    def evaluate(self):
        while self.expression.size != 0:
            item = self.expression.remove_front()
            print(item)

            if type(item) == MixedFraction:
                self.stack.add_front(item)

            elif item in self.ops:
                op1 = self.stack.remove_front()
                op2 = self.stack.remove_front()
                print(op1, op2)
                product = self.ops[item](op2, op1)
                self.stack.add_front(product)

        res = self.stack.remove_front()
        return res


pe = EvaluateMixedFraction()
pe.input("3/2")
pe.input("1 2/3")
pe.input("+")
assert pe.evaluate() == MixedFraction(1, 6, 3)

pe.input("1/2")
pe.input("2/3")
pe.input("+")
pe.input("1 1/8")
pe.input("-")
assert pe.evaluate() == MixedFraction(1, 24)

pe.input("1 1/2")
pe.input("2 2/3")
pe.input("+")
pe.input("1 1/6")
pe.input("-")
pe.input("5/4")
pe.input("*")
assert pe.evaluate() == MixedFraction(3, 4, 3)
# ee = EvaluatePostfix()
# ee.input('1')
# ee.input('2')
# ee.input('+')
# assert ee.evaluate() == 3
# pe = EvaluateFraction()
# pe.input("1/2")
# pe.input("2/3")
# pe.input("+")
# print("PE Ev")
# assert pe.evaluate() == Fraction(7, 6)

# pe.input("1/2")
# pe.input("2/3")
# pe.input("+")
# pe.input("1/6")
# pe.input("-")
# assert pe.evaluate() == Fraction(1, 1)

# pe.input("1/2")
# pe.input("2/3")
# pe.input("+")
# pe.input("1/6")
# pe.input("-")
# pe.input("3/4")
# pe.input("*")
# assert pe.evaluate() == Fraction(3, 4)
