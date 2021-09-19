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
    if arr[l] > arr[r]:
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
    for i in range(i, 0, -1):  # iterate left
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
