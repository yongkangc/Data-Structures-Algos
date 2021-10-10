from abc import ABC, abstractmethod

# Not implemented with interface


class LightBox():
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

# Implementing with interface


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


class LightBoxSM(StateMachine):

    def __init__(self):
        self.start_state = "off"

    def get_next_values(self, state, inp):

        if state == "off":
            if inp == 1:
                next_state = "on"
            else:
                next_state = "off"
        elif state == "on":
            if inp == 1:
                next_state = "off"
            else:
                next_state = "on"
        output = next_state
        return next_state, output


lb2 = LightBoxSM()
lb2.start()
print(lb2.step(0))
print(lb2.step(0))
print(lb2.step(1))
print(lb2.step(0))
print(lb2.step(0))
print(lb2.step(0))
print(lb2.step(0))
print(lb2.step(1))
print(lb2.step(1))
print(lb2.step(1))
print(lb2.step(1))
print(lb2.step(0))
print(lb2.step(1))
