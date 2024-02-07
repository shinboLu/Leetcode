class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [[float('inf')] * 2 for _ in range(n+1)]

        dp[0] = [0,0]

        ## i = floor_id
        for i in range(1,n+1):
            dp[i][0] = i
            ## choose (1,i+1) to throw the second egg
            for j in range(1, i+1):
                ## if 2nd egg broke at k: dp[i][1] = dp[k-1][0] + 1
                ## if 2nd egg didn't break: dp[i][1] = dp[i-k][1] + 1
                dp[i][1] = min(dp[i][1], max(dp[j-1][0], dp[i-j][1]) + 1)

        return dp[n][1]
