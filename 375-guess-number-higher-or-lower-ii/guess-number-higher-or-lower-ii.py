class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] represents the minimum amount of money needed to guarantee a win 
        #       when guessing a number between i and j inclusive.

        dp = [[0] * (n+2) for _ in range(n+2)]

        for d in range(1, n+1):
            for i in range(1, n-d+1):
                j = i+d
                dp[i][j] = float('inf')
                for k in range(i, j+1):
                    cost = max(dp[i][k-1], dp[k+1][j]) + k
                    dp[i][j] = min(dp[i][j], cost) 

        return dp[1][n]