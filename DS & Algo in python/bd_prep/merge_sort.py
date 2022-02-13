
def merge_sort(arr):
    n = len(arr)

    # base case
    if n == 1:
        return arr
    mid = n // 2
    # the inituition is that we want to break up into left and right for each ieration

    left = merge_sort(arr[mid:])
    right = merge_sort(arr[:mid])
    return merge(left, right)


def merge(left_arr, right_arr):
    left, right = 0, 0
    res = []

    while left < len(left_arr) and right < len(right_arr):  # have not finished traversal
        print(left_arr, right_arr)
        if left_arr[left] < right_arr[right]:
            res.append(left_arr[left])
            left += 1

        else:
            res.append(right_arr[right])
            right += 1

    if left >= len(left_arr):
        print(res)
        res += right_arr[right:]
        print(res)
    elif right >= len(right_arr):
        print(res)

        res += left_arr[left:]
        print(res)

    return res


# def merge_sort(array):
#     if len(array) == 1:
#         return array
#     mid = len(array)//2
#     left = merge_sort(array[:mid])
#     right = merge_sort(array[mid:])
#     return merge(left, right)


# def merge(arr_1, arr_2):
#     combined = []
#     i, j = 0, 0
#     while i <= len(arr_1)-1 and j <= len(arr_2)-1:
#         if arr_1[i] < arr_2[j]:
#             combined.append(arr_1[i])
#             i += 1
#             last = 'i'
#         else:
#             combined.append(arr_2[j])
#             j += 1
#             last = 'j'

#     if last == 'i':
#         combined += arr_2[j:]
#     else:
#         combined += arr_1[i:]
#     return combined


# Test case
if __name__ == '__main__':
    arr = [5, 2, 4, 6, 1, 3]
    print(merge_sort(arr))
    assert merge_sort(arr) == [1, 2, 3, 4, 5, 6]
