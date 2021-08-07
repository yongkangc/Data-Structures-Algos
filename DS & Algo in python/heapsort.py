# heap sort
#
# Description:
# Heapsort is an in-place sorting algorithm that is based on the heaps data structure.
# Heapsort can be thought of as an improved selection sort: like that algorithm,
# it divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region
# by extracting the largest element and moving that to the sorted region.
# The O(n log n) time complexity of heapsort makes it an efficient algorithm for sorting in situations
# where n is much greater than the number of elements in the array.
#

import heapq 

def heapsort(iterable):
    for value in iterable:
        heapq.heappush(iterable, value)
    return [heapq.heappop(iterable) for i in range(len(iterable))]
