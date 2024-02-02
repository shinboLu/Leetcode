class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dp = [row for row in mat]
        nrow, ncol = len(mat), len(mat[0])

        for row in range(nrow):
            for col in range(ncol):
                min_dist = float('inf')
                if dp[row][col] != 0:
                    if row > 0: 
                        min_dist = min(min_dist, dp[row-1][col])
                    if col > 0: 
                        min_dist = min(min_dist, dp[row][col-1])
                    dp[row][col] = min_dist + 1 

        for row in range(nrow-1, -1, -1):
            for col in range(ncol-1, -1, -1):
                min_dist = float('inf')
                if dp[row][col] != 0:
                    if row < nrow-1:
                        min_dist =min(min_dist, dp[row+1][col])
                    if col < ncol -1:
                        min_dist = min(min_dist, dp[row][col+1])

                    dp[row][col] = min(dp[row][col], min_dist+1)

        return dp
