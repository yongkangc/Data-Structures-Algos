# copy your solution for MyAbstractList from the Cohort problems

import collections.abc as c


class MyAbstractList(c.Iterator):
    size = 0
    _idx = 0

    def __init__(self, list_items):
        for item in list_items:
            print(item)
            self.append(item)

    @property
    def is_empty(self):
        return self.size == 0

    def append(self, item):
        self.add_at(self.size, item)

    def remove(self, item):
        if item not in self:
            return None
        self.remove_at(self.index_of(item))

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        self.set_at(index, value)

    def __delitem__(self, index):
        self.remove_at(index)

    def __len__(self):
        return self.size

    def __iter__(self):
        self._idx = 0
        return self

    def __next__(self):
        if self._idx < self.size:
            n_item = self.get(self._idx)
            self._idx += 1
            return n_item
        else:
            raise StopIteration


class Node:
    def __init__(self, e):
        self.element = e
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if isinstance(value, Node):
            self.__next = value


class MyLinkedList(MyAbstractList):
    def __init__(self, items):
        self.head = None
        self.tail = None
        super().__init__(items)

    def get(self, index):
        print(index)

        counter = 0
        curr = self.head
        while counter <= index:
            if counter == index:
                print(curr.next.element)

                return curr.element
            counter += 1
            curr = curr.next

    def add_first(self, element):
        node = Node(element)
        self.head = node

        if not self.tail:
            self.tail = node

        self.size += 1

    def add_last(self, element):
        node = Node(element)
        self.size += 1

        if not self.tail:
            self.head = node
            self.tail = node

        else:
            prev_tail = self.tail
            self.tail = node
            prev_tail.next = node

    def add_at(self, index, element):
        if index == 0:
            self.add_first(element)

        elif index >= self.size:
            self.add_last(element)
        else:
            counter = 0
            curr = self.head
            while curr.next is not None and counter <= index:
                if counter == index:
                    node = Node(element)
                    curr_next = curr.next
                    curr.next = node
                    node.next = curr_next
                    self.size += 1
                else:
                    counter += 1
                    curr = curr.next

    def set_at(self, index, element):
        if 0 <= index < self.size:
            current = self.head
            for idx in range(0, index):
                current = current.next
            current.element = element

    def remove_first(self):
        if self.size == 0:
            # if list is empty, return None
            return None
        else:
            # otherwise, do the following:
            # 1. store the head at a temporary variable
            # 2. set the next reference of the current head to be the head
            # 3. reduce size by 1
            # 4. if the new head is now None, it means empty list
            #    -> set the tail to be None also
            # 5. return element of the removed node
            prev_head = self.head
            self.head = prev_head.next
            self.size -= 1
            if not self.head:
                self.tail = None
            return prev_head

    def remove_last(self):
        if self.size == 0:
            # if the list is empty, return None
            return None
        elif self.size == 1:
            prev_tail = self.tail
            self.tail = None
            self.head = None
            self.size -= 1
            return prev_tail
        else:
            curr = self.head
            while curr.next is not None:
                prev = curr
                curr = curr.next
            prev_tail = curr
            self.tail = prev
            prev.next = None
            self.size -= 1
            return prev_tail
            # otherwise, do the following:
            # 1. traverse to the second last node
            # 2. store the tail of the list to a temporary variable
            # 3. set the current node as the tail
            # 4. set the next ref of the tail to be None
            # 5. reduce the size by 1
            # 6. return the element of the removed node in the temp var

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            return None
        elif index == 0:
            return self.remove_first()
        elif index == self.size - 1:
            return self.remove_last()
        else:
            counter = 0
            curr = self.head
            while curr.next is not None and counter <= index:
                if counter == index:
                    prev.next = curr.next
                    curr.next = None
                    self.size -= 1

                    return curr
                else:
                    prev = curr
                    curr = curr.next

            # do the following:
            # 1. traverse to the node at index - 1
            # 2. get the node at index using next reference
            # 3. set the next node of the node at index - 1
            # 4. decrease the size by 1
            # 5. return the element that is removed


asean = MyLinkedList(['Singapore', 'Malaysia'])
assert asean.head.element == 'Singapore'
assert asean.tail.element == 'Malaysia'
print("Size" + str(asean.size))

asean.append('Indonesia')
assert asean.tail.element == 'Indonesia'
asean.add_at(0, 'Brunei')
assert asean.head.element == 'Brunei'
# print("Size" + str(asean.size))
assert asean.size == 4
assert len(asean) == 4

asean[0] = 'Cambodia'
print(asean[0])
assert asean[0] == 'Cambodia' and asean[1] == 'Singapore'
asean[2] = 'Myanmar'
assert(len(asean)) == 4
assert [x for x in asean] == ['Cambodia', 'Singapore', 'Myanmar', 'Indonesia']

del asean[0]
assert [x for x in asean] == ['Singapore', 'Myanmar', 'Indonesia']

asean.add_at(2, 'Brunei')
assert [x for x in asean] == ['Singapore', 'Myanmar', 'Brunei', 'Indonesia']
del asean[3]
assert [x for x in asean] == ['Singapore', 'Myanmar', 'Brunei']
del asean[1]
assert [x for x in asean] == ['Singapore', 'Brunei']
del asean[1]
assert [x for x in asean] == ['Singapore']
del asean[0]
assert [x for x in asean] == []
