class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        nrow = len(s)
        ncol = len(t)

        dp = [[0] * (ncol +1) for _ in range(nrow+1)]
        for i in range(nrow+1):
            dp[i][ncol] = 1

        for i in range(nrow-1, -1, -1):
            for j in range(ncol-1, -1, -1):
                dp[i][j] = dp[i+1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        return dp[0][0]

