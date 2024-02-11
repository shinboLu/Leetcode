class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## dp[i][0/1] stands for the at i-th day, the maxium profit from not holding and holding a stock
        ## dp[i][0] represents the maximum profit on day i with no stocks held
        ## dp[i][1] represents the maximum profit on day i with stocks held

        n = len(prices)
        dp = [[float('-inf')] * 2 for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], prices[i] + dp[i-1][1])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return max(dp[-1][0], 0)
