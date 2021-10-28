from collections import OrderedDict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        if not formula:
            return ""
        counter = OrderedDict()
        stack = Stack()
        for char in formula:
            stack.push(char)

        mult = 1
        bracket_mult = 1
        concat_elem = ""
        in_brackets = False
        curr = {}  # dict to holda the current elements before update

        while stack.peek():
            char = stack.pop()
            if char.isnumeric():
                if stack.peek() == ")":
                    bracket_mult *= int(char)
                else:
                    mult *= int(char)

            elif char == ")":
                in_brackets = True

            elif char == "(":
                for k, v in curr.items():
                    counter[k] = counter.get(
                        k, 0) + v * bracket_mult  # update counter
                curr = {}

                in_brackets = False
                mult = 1
                bracket_mult = 1

            elif char.islower():
                # add the char to the concat Elem
                concat_elem += char

            elif char.isupper():
                # form a word with concat_elem
                elem = char + concat_elem
                curr[elem] = curr.get(elem, 1) * mult

                # reset concat_elem
                concat_elem = ""
                mult = 1

                if not in_brackets:
                    counter = self.update_counter(counter, curr)
                    curr = {}
                    # add all the elements from the bracket to

        formula_str = ""
        for k, v in counter.items():
            formula_str += k + str(v)
        return formula_str

    def update_counter(self, counter, curr):
        for elem in curr:
            counter[elem] = counter.get(elem, 0) + curr[elem]
        return counter


class Stack:
    def __init__(self):
        self.data = []

    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop(-1)

    def push(self, val):
        self.data.append(val)

    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[-1]

    def __str__(self):
        return str(self.data)
