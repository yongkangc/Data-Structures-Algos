Question
`Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.`

1. [Two pointers](#two-pointers)
1. [Two Pointers with hashset](#two-pointers-with-hashset)
1. [Two pointers without sort](#two-pointers-without-sort)

## Two pointers

1. create a target array and sort it so that we can skip the target if it is the same as previous one.
1. sort the nums array, and iterate through the nums array.
1. Use two pointers and while the left pointer is less than the right pointer, we continue to iterate through the nums array.
1. if the sum of two pointer is less than the target, move the left pointer to the right. If more we move right pointer.
1. increase left as we have covered
1. To avoid duplicates, we increase

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        res = []
        nums.sort()

        # convert 3 sum problem into 2 sum problem
        for i,target in enumerate(nums):
            if i > 0 and target == nums[i - 1] : # skip target duplicate
                continue
            # use a 2 pointer method to find the target
            left,right = i + 1,len(nums) - 1
            while left < right:
                two_sum = target + nums[left] + nums[right]
                print(target,nums[left],nums[right])
                if two_sum < 0:
                    left += 1
                elif two_sum > 0:
                    right -= 1
                else:
                    res.append([target,nums[left],nums[right]])
                    # converge the left and right, so no infinite loop occurs
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1 # move left pointer forward if it was the same as the previous one


        return res

```

## Two pointers with hashset

## Two pointers without sort
