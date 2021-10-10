class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{} is {} years old'.format(self.name, self.age)

    def __repr__(self):
        return 'Person({}, {})'.format(self.name, self.age)


class People(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


test = People('John', 30)
print(test.name, test.age)
