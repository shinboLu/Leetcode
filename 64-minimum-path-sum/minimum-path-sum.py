class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nrow = len(grid) 
        ncol = len(grid[0])

        dp = [[0] * (ncol) for _ in range(nrow)] 
        dp[0][0] = grid[0][0]


        for i in range(1,nrow):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1, ncol):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, nrow):
            for j in range(1, ncol):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]
        