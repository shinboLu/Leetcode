class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(2, n+1):
            for j in range(1, i):
                if dp[i-j] == False and i % j == 0:
                    dp[i] = True

        return dp[-1]
