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


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        curr = arr[i]
        j = i - 1
        while curr < arr[j] and j >= 0:
            arr[j] = arr[j+1]  # shift right rightwards
            j -= 1
    return arr


arr = [randint(0, 100) for p in range(0, 10)]
insertion_sort(arr) == sorted(arr)
print(insertion_sort(arr))
