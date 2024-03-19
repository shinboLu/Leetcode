class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        res = 0

        for i in range(len(s)-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        res += 1
                        dp[i][j] = True 
                    elif dp[i+1][j-1]:
                        res += 1
                        dp[i][j] = True 
        return res 