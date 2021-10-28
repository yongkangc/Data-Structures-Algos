

def mergesort(array):
    # split array into 2
    mid = len(array)//2
    mergesort_recursive(array, 0, len(arr)-1)


# From pseudo code in the ddw notes
def mergesort_recursive(arr, p, r):
    """
    p: index of beginning of array
    r : index of the end of array
    """
    # base case array contains only 1 element -> trivally sorted, so all we need to do is to merge

    # question : when do we merge the array of index 1?
    if r-p + 1 > 1:
        q = (p+r)//2  # split the array
        merge_sort(arr, p, q)  # first half
        merge_sort(arr, q+1, r)  # second half
        merge(arr, p, q, r)


def merge(arr, p: int, q: int, r: int):
    """
    Merge the 2 arrays on left and right which are already sorted
    In place merging

    p : beginning index of the left array. This is also the beginning of the 
    q : ending index of the left array. q+1 is the starting index of the right array
    r : ending index of the right array.

    The idea is to start from the beginning of the left and right arrays and compare the 2 arrays pointed by the left and right arrow. 
    The smaller number will be placed in position pointed by dest
    """
    n_left_arr = q - p + 1  # length of the left arr
    n_right_arr = r-q  # r - (q+1) +1

    print(n_left_arr, n_right_arr)

    left_arr = arr[p:q+1]
    right_arr = arr[(q+1):r+1]

    left = 0
    right = 0
    dest_i = p  # starting with the left of the sequence
    print(f"left arr {left_arr}, right arr {right_arr}")

    while left < n_left_arr and right < n_right_arr:

        # comparison of left and right pointer and appending the smallest one to index
        if left_arr[left] <= right_arr[right]:
            arr[dest_i] = left_arr[left]
            left += 1
        else:
            arr[dest_i] = right_arr[right]
            right += 1
        dest_i += 1

    while left < n_left_arr:
        arr[dest_i] = left_arr[left]
        left += 1
        dest_i += 1

    while right < n_right_arr:
        arr[dest_i] = right_arr[right]
        right += 1
        dest_i += 1
