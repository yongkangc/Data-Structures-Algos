from typing import List

"""
The idea for insertion sort is that you want to keep the smallest card in index zero and the rest of the 
numbers you would want to shift it leftwards. 
The stop condition is by the time you get to the last number, the array should be sorted.

Time complexity: O(n^2) as it is like ap operation
1 + 2 + .... n - 1 -> 
"""
def insertion_sort(arr: List[int]) -> List[int]:
  length = len(arr)
  for i in range(1,length):
    curr_val = arr[i]
    for j in range(i, 0, -1):
      comp_val = arr[j]
      if curr_val < comp_val:
        arr[i], arr[j] = arr[j], arr[i]

  return arr

def test():
  arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
  assert insertion_sort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  # print(insertion_sort(arr))

if __name__ == "__main__":
  test()