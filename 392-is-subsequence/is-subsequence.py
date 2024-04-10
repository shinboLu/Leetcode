class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        nrow = len(s) 
        ncol = len(t)

        dp = [[0] * (ncol+1) for _ in range(nrow+1)]

        ## dp[i][j] = at s[i], t[j] has a matching char 

        for i in range(1, nrow+1):
            for j in range(1, ncol+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        if dp[-1][-1] == len(s):
            return True 

        return False 