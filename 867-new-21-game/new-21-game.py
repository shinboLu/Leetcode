class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        #dp[i] the possibility of reach k at ith draw

        dp = [None] * (k+maxPts)

        window_sum = 0

        for i in range(k, k+maxPts):
            dp[i] = 1 if i <= n else 0
            window_sum += dp[i] 

        for i in range(k-1, -1,-1):
            dp[i] = window_sum / maxPts
            window_sum = window_sum - dp[i+maxPts] + dp[i] 

        return dp[0]