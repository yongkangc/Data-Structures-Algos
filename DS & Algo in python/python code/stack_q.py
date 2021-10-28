import operator


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop(-1) if not self.is_empty else None

    def peek(self):
        if self.is_empty:
            return None
        return self.__items[-1]

    @property
    def is_empty(self):
        return len(self.__items) == 0

    @property
    def size(self):
        return len(self.__items)


class QueueList:

    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0) if not self.is_empty else None

    def peek(self):
        if self.is_empty:
            return None
        return self.__items[0]

    @property
    def is_empty(self):
        return len(self.__items) == 0

    @property
    def size(self):
        return len(self.__items)


class Queue:
    """ Queue using 2 stacks instead of python lists"""

    def __init__(self):
        self.left_stack = Stack()
        self.right_stack = Stack()

    @property
    def is_empty(self):
        return self.left_stack.is_empty and self.right_stack.is_empty

    @property
    def size(self):
        return self.left_stack.size + self.right_stack.size

    def enqueue(self, item):
        self.right_stack.push(item)

    def dequeue(self):
        if self.left_stack.is_empty:
            while not self.right_stack.is_empty:
                self.left_stack.push(self.right_stack.pop())
        return self.left_stack.pop()

    def peek(self):
        if self.left_stack.is_empty:
            while not self.right_stack.is_empty:
                self.left_stack.push(self.right_stack.pop())
        x = self.left_stack.peek()
        return x


class Dequeue(Queue):

    def add_front(self, item):
        """Add item to the front of the queue"""
        # push all items from right_stack to left_stack
        while not self.right_stack.is_empty:
            self.left_stack.push(self.right_stack.pop())
        self.left_stack.push(item)
        # push all items from left_stack to right_stack
        while not self.left_stack.is_empty:
            self.right_stack.push(self.left_stack.pop())

    def remove_front(self):
        """Remove item from the front of the queue"""
        return self.dequeue()

    def add_rear(self, item):
        self.enqueue(item)

    def remove_rear(self):
        return self.right_stack.pop()

    def peek_front(self):
        return self.peek()

    def peek_rear(self):
        return self.right_stack.peek()
