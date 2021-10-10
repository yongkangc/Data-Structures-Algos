class RadixSort:

    def __init__(self, MyList: list):
        self.items = MyList
        self.main_bin = Queue()
        self.radix_bins = [Queue() for i in range(10)]

    def max_digit(self):
        # Returns the maximum number of digit in the list
        return max([len(str(i)) for i in self.items])

    def convert_to_str(self, items):
        max_digit = self.max_digit()
        for i in range(len(self.items)):
            print(i, self.items[i])
            self.items[i] = str(items[i]).zfill(max_digit)

    def sort(self):
        res = []
        # find the maximum digit
        max_digit = self.max_digit()
        # convert all the items to strings and put them in the main bin
        self.convert_to_str(self.items)
        for i in self.items:
            self.main_bin.enqueue(i)

        for i in range(max_digit - 1, -1, -1):
            # put the items in the corresponding radix bin as per i
            while not self.main_bin.is_empty:
                item = self.main_bin.dequeue()
                self.radix_bins[int(item[i])].enqueue(item)
                print(self.radix_bins[i].items)

            # dequeue the items from the radix bin and put them in the main bin
            for j in range(len(self.radix_bins)):
                radix_bin = self.radix_bins[j]
                while not radix_bin.is_empty:
                    self.main_bin.enqueue(radix_bin.dequeue())

        # return the sorted list
        while not self.main_bin.is_empty:
            res.append(int(self.main_bin.dequeue()))

        return res


class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0) if not self.is_empty else None

    def peek(self):
        return self.__items[0]

    @property
    def items(self):
        return self.__items

    @property
    def is_empty(self):
        return len(self.__items) == 0

    @property
    def size(self):
        return len(self.__items)


list1 = RadixSort([10111, 26, 7, 10])
list2 = RadixSort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(max([len(str(i)) for i in [10111, 2, 3, 4, 26, 7, 8, 9, 10]]))
print(list1.sort())
