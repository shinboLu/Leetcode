class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        nrow = len(matrix)
        ncol = len(matrix[0])

        dp = [[0] * (ncol) for _ in range(nrow)]
        count = 0 
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    count += dp[i][j]


        return count