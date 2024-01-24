class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nrow = len(matrix)
        ncol = len(matrix[0])

        dp = [[0] * (ncol+1) for _ in range(nrow+1)] 

        max_side = 0

        for i in range(1, nrow+1):
            for j in range(1, ncol+1):
                if matrix[i-1][j-1] == '1': 
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) +1
                    max_side = max(max_side, dp[i][j])


        return max_side * max_side
