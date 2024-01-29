class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        nrow = len(mat) 
        ncol = len(mat[0])

        dp = [[(0, 0, 0, 0)] * (ncol + 2) for _ in range(nrow + 1)]
        res = 0
        for i in range(1, nrow+1):
            for j in range(1, ncol+1):
                if mat[i-1][j-1] == 1:
                    dp[i][j] = (dp[i][j-1][0] + 1, dp[i-1][j][1] + 1, dp[i-1][j-1][2] + 1, dp[i-1][j+1][3] + 1)
                    res = max(max(dp[i][j]), res)
        return res 
