Key concept: 
- there are two possible ways to rotate a sorted array:
    - left or right
    - we have to check whether target is in the left sorted array or the right sorted array

- After that use binary search with case to find the target
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums) - 1
        
        while left <=right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            # [4,5,6,7,0,1,2] # left sorted portion : [4,5,6,7] right sorted portion : [0,1,2]
            if nums[left] <= nums[mid]: # left sorted portion
                if target < nums[left] or target > nums[mid]: # target < lowest of lsp -> move right
                    left = mid + 1
                else:
                    right = mid - 1 # it is on the other side
            
            else: # right sorted portion
                if target > nums[right] or target < nums[mid]:
                    right = mid -1 
                else:
                    left = mid + 1
        return -1
```