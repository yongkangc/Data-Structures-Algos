
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        print('Animal moves')


class Cat(Animal):
    def move(self):  # if this function is not implemented, there would be error
        # this add new implementation to the class from abstract base class
        print("move")
        super().move()  # this calls the super function implementation as well


c = Cat()
c.move()
