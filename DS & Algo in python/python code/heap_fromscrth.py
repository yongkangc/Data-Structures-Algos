def get_parent(i):
    """  Return the parent node of index i   """
    return (i-1)//2


def get_left_child(i):
    """ Return the left child node of index i. """
    return 2*i + 1


def get_right_child(i):
    """ Return the right child node of index i. """
    return 2*i + 2


def get_max_child(arr, l, r):
    """Returns the index of the larger child node"""
    if r >= len(arr):
        return l
    elif arr[l] > arr[r]:
        max_child_i = l
    else:
        max_child_i = r
    return max_child_i


def heapify_non_optimized(arr, i):
    """ 
    Maintains the max heap property. 

    :params arr: the array to be heapified
    :params i: the index of the node to be heapified
    """
    curr = i
    l = get_left_child(i)

    while l < len(arr):  # traverse down the height of the tree until the end
        l = get_left_child(i)
        r = get_right_child(i)

        max_child_i = get_max_child(arr, l, r)

        if arr[max_child_i] > arr[i]:
            arr[max_child_i], arr[i] = arr[i], arr[max_child_i]
        curr = max_child_i  # moving down


def heapify(arr, i):
    """ 
    Maintains the max heap property. 

    :params arr: the array to be heapified
    :params i: the index of the node to be heapified

    The optimized version checks if the largest child is already less than the current node
    """
    curr = i
    l = get_left_child(i)
    swapped = True

    while l < len(arr) and swapped:  # traverse down the height of the tree until the end
        swapped = False
        l = get_left_child(i)
        r = get_right_child(i)

        max_child_i = get_max_child(arr, l, r)

        if arr[max_child_i] > arr[i]:
            arr[max_child_i], arr[i] = arr[i], arr[max_child_i]
            swapped = True
        curr = max_child_i  # moving down


# Building heap
# The idea is to go through every nodes in the tree and heapify them. However, we need not do for all the nodes, but rather only half of those nodes.
# So we start from the middle and iterate left wards. Middle represents one layer above the leaf nodes. Logn
def build_heap(arr):
    n = len(arr)
    mid = n//2
    # start building arr from the level above the leaf node all the way up
    for i in range(mid, -1, -1):  # iterate left
        heapify(arr, i)

    return arr


def heap_sort(heap):
    sorted = []

    while heap:
        sorted.append(heap.pop(0))
        heap = heapify(heap)


def heap_sort_v2(arr):
    heap = build_heap(arr)
    heap_end_pos = len(arr)

    while heap_end_pos > 0:
        # start from the last element in the heap and swap it with the largest element (always at index 0).
        arr[0], arr[heap_end_pos] = arr[heap_end_pos]
        heap_end_pos = heap_end_pos - 1  # reduce heap size
        heap = heapify(arr[:heap_end_pos])


# questions for prof
# 1. It might make more sense to do a postorder traversal and bubble up from leaf node than to start at the the node above the leaf. which is a better approach? # recurvise vs iterative
# why do we want to swap the last element in the heap? other than we want to keep the order?
# would creating a new list and putting the min there be faster? i.e calling extract min and heapify?
# array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

# build_heap(array)
# print(array)
# assert array == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
def heapsort(array):
    ###
    # YOUR CODE HERE
    ###
    n = len(array) - 1
    build_max_heap(array)
    while n > 0:
        print(f"Before swa heap {array}")

        array[0], array[n] = array[n], array[0]
        n -= 1
        print(f"n {n}")
        print(f"After swa heap {array}")

        array[:n+1] = max_heapify(array[:n+1], 0, len(array[:n+1]))
        print(f"After max heap {array}")
        print("==============================\n")


def heap_sort_michael(array):
    build_max_heap(array)
    heap_end_pos = len(array)-1
    while heap_end_pos > 0:
        print(array)
        array[0], array[heap_end_pos] = array[heap_end_pos], array[0]
        heap_end_pos -= 1
        max_heapify(array, 0, heap_end_pos+1)


def build_max_heap(array):
    ###
    # YOUR CODE HERE
    ###
    size = len(array)
    mid = size//2
    for i in range(mid, -1, -1):
        max_heapify(array, i, size)


def max_heapify(array, i, size):

    curr = i
    swapped = True

    while left_of(curr) < size and swapped:
        swapped = False
        max_child_i = max_child(array, curr, size)
        if array[curr] < array[max_child_i]:
            swapped = True
            array[curr], array[max_child_i] = array[max_child_i], array[curr]
        curr = max_child_i
    return array


def left_of(index):
    return 2*index + 1


def right_of(index):
    return 2*index + 2


def max_child(array, index, heap_size):

    left_child = left_of(index)
    right_child = right_of(index)
    if right_child >= heap_size:
        return left_child
    elif array[left_child] >= array[right_child]:
        return left_child
    else:
        return right_child


array = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
heap_sort_v2(array)
print(array)
assert array == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
