```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s : return 0
        n = len(s)
        # we need to set an empty slot to allow for extra space
        dp = [0] * (n+1) 
        dp[0] = 1 # empty offset for dp[i-2]
        dp[1] = 0 if s[0] == '0' else 1
        
        
        # let dp[i] be the maximum number of ways we can decode s[1:i+1]
#         bottom up recurrence
#         dp[i] = dp[i-1] + dp[i-2]
        
#         for each index, we can either choose that index or the index with the one on the right
#         this is similar to the house robber problem
#         memoise the result
        
        # for each index, we can choose that word to decode or the word with its neighbor
        for i in range(2, n + 1):
            # decode single word in the previous index
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # decode word in the index 2 before 
            if 10<=int(s[i-2 : i]) <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]
```