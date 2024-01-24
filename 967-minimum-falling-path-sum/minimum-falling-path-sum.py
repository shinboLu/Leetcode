class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]

        # dp init
        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(1, n):
            for j in range(n):
                
                cur = dp[i-1][j] 

                if j - 1 >= 0:
                    cur = min(cur, dp[i-1][j-1])

                if j + 1 < n:
                    cur = min(cur, dp[i-1][j+1])

                dp[i][j] = cur + matrix[i][j]
 
        return min(dp[-1])