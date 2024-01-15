class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        nrow = len(text1)
        ncol = len(text2)

        dp = [[0] * (ncol+1) for _ in range(nrow+1)]

        for i in range(nrow-1, -1, -1):
            for j in range(ncol-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]