class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        dp = [0,0,0]

        for i in range(len(costs)):
            dp1 = min(dp[1], dp[2]) + costs[i][0]
            dp2 = min(dp[0], dp[2]) + costs[i][1]
            dp3 = min(dp[0], dp[1]) + costs[i][2]

            dp = [dp1, dp2, dp3]
        return min(dp)


