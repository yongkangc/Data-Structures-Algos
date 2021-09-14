Link to problem : <https://leetcode.com/problems/greatest-sum-divisible-by-three/>

Intuition:
1.The last maximum possible sum that it is divisible by three could only depends
on 3 kinds of "subroutines/subproblems": 1. previous maximum possible sum that it is divisible by three
preSum % 3 == 0 (example: preSum=12 if lastNum=3) 2. preSum % 3 == 1 (example: preSum=13 if lastNum=2) 3. preSum % 3 == 2 (example: preSum=14 if lastNum=1) 2. This recusion + "subroutines" pattern hints Dynamic Programming

    dp state:
        dp[i] = max sum such that the remainder == i when sum / 3
    Transition:
        dp_cur[(rem + num) % 3]
            = max(dp_prev[(rem + num) % 3], dp_prev[rem]+num)
            where "rem" stands for remainder for shorter naming
        meaning:
            "Current max sum with remainder 0 or 1 or 2" could be from
            EITHER prevSum with remainder 0 or 1 or 2 consecutively
            OR     prevSum with some remainder "rem" + current number "num"

            Since (dp_prev[rem]+num) % 3 = (rem+num) % 3 = i, we are able to correctly
            update dp[i] for i = 1,2,3 each time

```python
def maxSumDivThree(self, nums: List[int]) -> int:
 n = len(nums)
 dp = [[0]*3 for _ in range(n+1)]
 dp[0][1] = float('-inf')
 dp[0][2] = float('-inf')
 for i in range(1, n+1):
  if nums[i-1] % 3 == 0: # Current remainder == 0
   dp[i][0] = max(dp[i-1][0], dp[i-1][0] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][0] to keep the remainder 0
   dp[i][1] = max(dp[i-1][1], dp[i-1][1] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][1] to keep the remainder 1
   dp[i][2] = max(dp[i-1][2], dp[i-1][2] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][2] to keep the remainder 2
  elif nums[i-1] % 3 == 1: # Current remainder == 1
   dp[i][0] = max(dp[i-1][0], dp[i-1][2] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][2] to keep the remainder 0
   dp[i][1] = max(dp[i-1][1], dp[i-1][0] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][0] to keep the remainder 1
   dp[i][2] = max(dp[i-1][2], dp[i-1][1] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][1] to keep the remainder 2
  else: # Current remainder == 2
   dp[i][0] = max(dp[i-1][0], dp[i-1][1] + nums[i-1]) # Can you tell how this works now?
   dp[i][1] = max(dp[i-1][1], dp[i-1][2] + nums[i-1])
   dp[i][2] = max(dp[i-1][2], dp[i-1][0] + nums[i-1])

 return dp[-1][0]
```

### My understanding
