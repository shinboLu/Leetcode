class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        nrow = len(s)
        ncol = len(t)

        dp = [[0] * (ncol+1) for _ in range(nrow+1)]

        for i in range(nrow-1, -1, -1):
            for j in range(ncol-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        if dp[0][0] == len(s):
            return True
        else:
            return False