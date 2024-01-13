class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nrow = len(matrix) 
        ncol = len(matrix[0])

        dp = [[0] * (ncol+1) for _ in range(nrow+1)]
        max_side = 0
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j], dp[i][j+1])+1
                    max_side = max(max_side, dp[i+1][j+1])

        return max_side * max_side



                    