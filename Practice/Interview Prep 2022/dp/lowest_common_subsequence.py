class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # compare two characters, if they are equal, we can move to the next subproblem comparing str[i+1:]
        
        # let dp(i,j) be the LCS of text1[:i] and text2[:j]
        
        # if xi == yj,  dp[i,j] = dp[i-1, j-1] + xi
        
        # eg lcs(aab,azb) -> 1 + lcs(aa,az) ->  1 + max((a,az) , lcs(aa,a))
        
        # else, either at least one of the 2 subsequences dp(i-1,j) or dp(i,j-1) is the LCS of text1 & text2
        
        # base case is if one of the str is empty -> return 0
        
        
        # 2d cache of all possible substring for each text
        dp = [[0 for _ in range(0, len(text2) + 1)] for _ in range (0, len(text1) + 1)]

        
        # start from (1,1)
        for i in range(0,len(text1) + 1):
            for j in range(0,len(text2) + 1):
                if i == 0 or j == 0: 
                    continue
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                
                else:
                    # there are two possible case, we can skip i or we can skip j
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[len(text1)][len(text2)]
                