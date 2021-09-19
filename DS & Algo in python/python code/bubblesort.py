# 19/9/21
# Description: Bubble Sort
# Going to try it without referring to pseudocode


from random import randint
import random
from functools import wraps
from time import time
from random import randrange


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        # print('func:%r args:[%r, %r] took: %2.4f sec' %
        #       (f.__name__, args, kw, te-ts))
        print('func:%r took: %2.4f sec' %
              (f.__name__, te-ts))
        return result
    return wrap


@timing
def bubble_sort(arr):
    swapped = True
    end = len(arr)
    curr = end
    while swapped:
        swapped = False
        for i in range(1, end):
            # second_number = arr[i]
            # first_number = arr[i-1]
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]  # swap
                swapped = True
                curr = i
        end = curr
    return arr


@timing
def v4_bubble_sort(arr):
    n = len(arr)
    list_sorted = False
    while not list_sorted:
        list_sorted = True
        new_n = 0
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                list_sorted = False
                new_n = i  # updating latest sorted index
        n = new_n  # stop sorting as the next n elements are already sorted
    return arr


# assert bubble_sort([5, 4, 2, 3, 6, 1]) == [1, 2, 3, 4, 5, 6]

random.seed(10)


arr = [randint(0, 10) for p in range(0, 10)]
v4_bubble_sort(arr)
# bubble_sort(arr)
