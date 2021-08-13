There are 2 ways to solve this problem

1. [Greedy](#greedy)
2. [Dynamic Programming](#dynamic-programming)

### Greedy
Key concept: 
- start at the end of the array and see if we can jump to the start
- shift the end if the end position can be reached
- O(N) time , O(1) space

```python
def can_jump(nums):
    goal = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1): # start at the end
        if i + nums[i] >= goal: # if the jump length reach the goal
            goal = i # shift the goal if we can reach the end
    return goal == 0 # if we can reach the start
```


### Dynamic Programming

```python
# Below is the top-down approach

def Jump(nums, dp, ind):
    if nums[0]>=len(nums) or (nums[0]==0 and len(nums)==1): return True # [0] case
    if nums[0]==0: return False
    if dp[ind]!=None:
        print("dp used")
        return dp[ind]
    status = True
    for i in range(1, nums[0]+1):
        if i==1:
            status = Jump(nums[i:], dp, ind + i)
        else:
            status = status or Jump(nums[i:], dp, ind + i)
    dp[ind] = status
    return dp[ind]


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        t = list(set(nums))
        if len(t)==1 and t[0]>=1: return True
        dp = [None]*len(nums)
        return Jump(nums, dp, 0)

# --------------------------------------------------------------
# Below is the bottom-up approach

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[-1] = True
        for i in range(len(nums)-2,-1,-1):
            n = nums[i]
            if n==0:
                dp[i]=False
                continue
            for j in range(n, 0,-1): # [n,1] inclusive
                if i+j<len(dp) and dp[i+j]==True:
                    dp[i] = True
                    break
        # print(dp)
        return dp[0]
```