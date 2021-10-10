# Abstract Base Class

In Python, abstract base classes provide a blueprint for concrete classes. They don’t contain implementation. Instead, they provide an interface and make sure that derived concrete classes are properly implemented.

Example from Week 12 Lecture

Interface:

```python
from abc import ABC, abstractmethod

class StateMachine(ABC):

    def start(self):
        self.state = self.start_state

    def step(self, inp):
        ns, o = self.get_next_values(self.state, inp)
        self.state = ns
        return o

    @abstractmethod
    def get_next_values(self, state, inp):
        pass
```

Implementation:

```python

class LightBox:
    def __init__(self):
        self.state = "off"

    def set_output(self, inp):
        if inp == 1 and self.state == "off":
            self.state = "on"
            return self.state
        if inp == 1 and self.state == "on":
            self.state = "off"
            return self.state
        return self.state

    def transduce(self, list_inp):
        for inp in list_inp:
            print(self.set_output(inp))
```

Article on python interface: https://realpython.com/python-interface/

An abstract method is a method that’s declared by the Python interface, but it may not have a useful implementation. The abstract method must be overridden by the concrete class that implements the interface in question.
