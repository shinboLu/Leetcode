class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        ncol = len(text1)
        nrow = len(text2)

        dp = [[0] * (ncol+1) for _ in range(nrow+1)]

        for i in range(nrow-1, -1, -1):
            for j in range(ncol-1, -1, -1):
                if text2[i] == text1[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else: 
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        print(dp)
        return dp[0][0]