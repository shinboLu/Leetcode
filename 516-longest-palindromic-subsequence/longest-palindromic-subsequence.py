class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        palin_s = s[::-1]
        dp = [[0] * (n+1) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == palin_s[j]:
                    dp[i][j] = dp[i+1][j+1] + 1 
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1]) 
        return dp[0][0]
