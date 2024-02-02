class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        nrow = len(mat)
        ncol = len(mat[0])

        dp = [row for row in mat] 

        for i in range(nrow):
            for j in range(ncol):
                min_neigh = float('inf') 
                if dp[i][j] != 0:
                    if i > 0:
                        min_neigh = min(min_neigh, dp[i-1][j])

                    if j > 0: 
                        min_neigh = min(min_neigh, dp[i][j-1])

                    dp[i][j] = min_neigh + 1

        for i in range(nrow-1, -1, -1):
            for j in range(ncol-1, -1, -1):
                min_neigh = float('inf')
                if dp[i][j] != 0:
                    if i < nrow-1:
                        min_neigh = min(min_neigh, dp[i+1][j])
                    if j < ncol-1:
                        min_neigh = min(min_neigh,dp[i][j+1])

                    dp[i][j] = min(dp[i][j], min_neigh+1)

        return dp

        