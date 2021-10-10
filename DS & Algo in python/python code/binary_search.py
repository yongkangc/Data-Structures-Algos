# binary search
# bianry search is a search algorithm that finds the position of a target value within a sorted array.
# The algorithm works by searching the middle element of an array,
# comparing the target value to the middle element, and swapping the target value with the middle element if the target value is greater than the middle element.
# The algorithm repeats this process until the target value is found or the array is empty.
# The algorithm is a divide and conquer algorithm.

def binary_search(nums: List[int], target: int) -> int: ):
    mid=len(nums) // 2
    if nums[mid] == target:
        return mid

    if nums[mid] > target:
        return binary_search(nums[:mid], target)
    else:
        return binary_search(nums[mid+1:], target) + mid + 1


def binarySearchIterative( nums, target):
    left,right = 0,len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]: # search right arr
            left = mid + 1
        elif target < nums[mid]: # search left arr
            right = mid - 1


    return -1 if nums[left] != target else left