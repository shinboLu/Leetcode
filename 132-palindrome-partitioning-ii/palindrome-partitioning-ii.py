class Solution:
    def minCut(self, s: str) -> int:
        def isPalindrom(s):
            return s == s[::-1]

        n = len(s)
        dp = [n] * n

        for i in range(n):
            if isPalindrom(s[:i+1]):
                dp[i] = 0
                continue
            for j in range(i):
                if isPalindrom(s[j+1:i+1]):
                    dp[i] = min(dp[i], dp[j] +1)
        print(dp)
        return dp[n-1]
