import collections.abc as c

import collections.abc as c
import numpy as np


class ArrayFixedSize(c.Iterable):

    def __init__(self, size, dtype=int):
        self.__data = np.empty(size)
        self.__data = self.__data.astype(dtype)

    def __getitem__(self, index):
        return self.__data[index]

    def __setitem__(self, index, value):
        self.__data[index] = value

    def __iter__(self):
        return iter(self.__data)

    def __len__(self):
        return len(self.__data)

    def __str__(self):
        out = "["
        for item in self:
            out += f"{item:}, "
        if self.__data != []:
            return out[:-2] + "]"
        else:
            return "[]"


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


# creating a class PythonList inheriting from MyAbstractList
# this is just for testing the MyAbstractList class

class PythonList(MyAbstractList):
    data = []

    def __init__(self):
        self.data = []
        super().__init__(list(range(10)))

    def add_at(self, index, item):
        self.data.insert(index, item)
        self.size += 1

    def set_at(self, index, item):
        self.data[index] = item

    def remove_at(self, index):
        self.data.pop(index)
        self.size -= 1

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError()

    def index_of(self, item):
        try:
            idx = self.data.index(item)
            return idx
        except:
            return -1


class MyArrayList(MyAbstractList):
    INITIAL_CAPACITY = 16

    def __init__(self, items, dtype=int):
        size = len(items)
        self.data = ArrayFixedSize(MyArrayList.INITIAL_CAPACITY, dtype)
        idx = 0
        for item in items:
            self.add_at(idx, item)
            idx += 1

        # iterate over every items and call add(item)

        ###
        # YOUR CODE HERE
        ###

    def add_at(self, index, item):
        self.ensure_capacity()
        for idx in range(self.size, -1, -1):
            print(idx, index)
            if idx > index:
                # shift all the items by one for every position after the index.
                self.data[idx + 1] = self.data[idx]
            elif idx == index:
                self.set_at(idx, item)
                self.size += 1

    def set_at(self, index, value):
        print("setting")
        self.data[index] = value

    def remove_at(self, index):
        if 0 <= index < self.size:
            for idx in range(self.size):
                print(idx, index)
                if self.size - 1 > idx >= index:
                    self.data[idx] = self.get(idx+1)
                # do the following
                # 1. get the element at index
                # 2. copy the data by shifting it to the left from index to the end
                # 3. return the element at index
            self.size -= 1
        else:
            raise IndexError()

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError()

    def index_of(self, item):
        try:
            idx = 0
            for data in self.data:
                if data == item:
                    return idx
                idx += 1
        except:
            # if not found, return -1
            return -1

    def ensure_capacity(self):
        if self.size >= len(self.data):
            new_data = ArrayFixedSize(self.size * 2 + 1)
            self.copy(self.data, 0, new_data, 0)
            self.data = new_data

    def copy(self, source, idx_s, dest, idx_d):
        for idx in range(idx_s, len(source)):
            offset = idx - idx_s
            dest[idx_d + offset] = source[idx]

    def clear(self):
        self.data = ArrayFixedSize(MyArrayList.INITIAL_CAPACITY)
        self.size = 0

    def __str__(self):
        out = "["
        for idx in range(self.size):
            out += f"{self.get(idx):}, "
        return out[:-2] + "]"


def test_myarr_list():
    a = MyArrayList([1, 2, 3])

    assert [x for x in a] == [1, 2, 3]
    assert a.size == 3
    assert not a.is_empty
    a.append(4)
    assert a.size == 4
    assert [x for x in a] == [1, 2, 3, 4]
    assert [a[i] for i in range(len(a))] == [1, 2, 3, 4]
    a[0] = -1
    assert [x for x in a] == [-1, 2, 3, 4]
    del a[0]
    print([x for x in a])
    assert [x for x in a] == [2, 3, 4]


def test_pylist():
    f = PythonList()
    print(list(range(10)))
    print(f.data)
    # Testing init
    assert f.data == list(range(10))

    # Testing size property
    assert f.size == 10

    # Testing is_empty property
    assert not f.is_empty

    # Testing add method
    f.append(10)
    assert f.data == list(range(11))

    # Testing remove method
    f.remove(5)
    assert f.data == [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]
    f.add_at(5, 5)
    f.append(5)
    f.remove(5)
    print(f[0])
    print(f.data == [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 5])
    assert f.data == [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 5]
    assert not f.remove(11)

    # Testing getitem method
    assert [f[i] for i in range(len(f))] == [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 5]
    f[0] = -1
    assert [f[i] for i in range(len(f))] == [-1, 1, 2, 3, 4, 6, 7, 8, 9, 10, 5]

    # Testing delitem
    del f[0]
    assert f[0] == 1

    # Testing __next__
    assert [x for x in f] == [1, 2, 3, 4, 6, 7, 8, 9, 10, 5]
    # Testing __iter__
    assert [x for x in f] == [1, 2, 3, 4, 6, 7, 8, 9, 10, 5]


test_myarr_list()
