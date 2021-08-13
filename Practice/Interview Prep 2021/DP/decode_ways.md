Key Concept:
- Dfs + cache
- we can only take only either 1 or 2 digits

Recursion Relation:
- At each index, we can either choose to decode element at i or i:i+2
- If the current index is 0, the cache is 0

Brute Force: DFS 
- For each number, if the element is less than three, we can branch out to either itself or when it is combined
- at each index, can we decode one character out or 2 character out?
- if total is less than 26, it is accepted as a string
- Time: O(2^n) because at each point, we can make 2 decision.


Memoisation: DFS + Caching
- At each index we can store the total number of ways we can decode up til that index
- At the end of the cache, that would be the total number of ways (answer)
- Time: O(n)


```python
class Solution:
    def numDecodings(self,s):
        dp = {len(s): 1} # base case when it hits the end

        def dfs(i):
           
            if i in dp: # base case for when the end of the index is hit or i has been cache
                return dp[i]
            if s[i] == '0': # base case if the current element is 0, it is not a valid number
                return 0
            res = dfs(i + 1)  
            if i + 1 < len(s) and '10' <= s[i:i + 2] <= '26':
                res += dfs(i + 2)
            dp[i] = res # cache
            return res
        return dfs(0)
```

With O(n) Memoisation but with clearer logic

```

    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == "0": return 0
        if len(s) == 1 : return 1
        
        dp = [0] * len(s)
        dp[0] = 1 # since we have already checked for index 0
        
        if s[1] != "0":
            curr_string = s[0:2]
            if 10 <= int(curr_string) <=26:
                dp[1] = dp[0] + 1 
            else:
                dp[1] = dp[0]
        
        else: # when second digit is 0
            curr_string = s[0:2]

            if 10 <= int(curr_string) <=26:
                dp[1] = dp[0]
            else:
                dp[1] = 0
            
        
        for i in range(2,len(s)):
            if s[i] != "0":
                curr_string = s[i-1:i+1]
                if 10 <= int(curr_string) <=26:
                    dp[i] = dp[i-1] + dp[i-2] # the previous 2 that we have calculated so far
                else:
                    dp[i] = dp[i-1] # else itll just be what we have calculated before
        
            else: # when currrent digit is 0
                curr_string = s[i-1:i+1] # finding if the current element + previous element

                if 10 <= int(curr_string) <=26:
                    dp[i] = dp[i-2]
                else:
                    dp[i] = 0

        
        return dp[-1]

```

Iterative DP Solving this in O(1):

- Solving this with bottom up iterative approach
- we do not need to store all of the solution, we just need to store:
    `dp[i] = dp[i+1] + dp[i+2]`


```python
class Solution:
    def numDecodings(self,s):
        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1] + dp[i + 2] 
            if i + 1 < len(s) and '10' <= s[i:i + 2] <= '26':
                dp[i] += dp[i + 2]
        return dp[0]
```

Similar Questions:
- house robber

Reference:
https://www.youtube.com/watch?v=6aEyTjOwlJU&ab_channel=NeetCode

https://www.youtube.com/watch?v=YcJTyrG3bZs&ab_channel=BackToBackSWE

https://www.youtube.com/watch?v=THV546jNCrw&ab_channel=thecodingworld
