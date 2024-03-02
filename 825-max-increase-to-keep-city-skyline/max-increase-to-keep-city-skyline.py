class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        nrow = len(grid) 
        ncol = len(grid[0])

        rows_max = [0] * nrow 
        cols_max = [0] * ncol 
        res = 0
        for i in range(nrow):
            for j in range(ncol):
                rows_max[i] = max(rows_max[i], grid[i][j])
                cols_max[j] = max(cols_max[j], grid[i][j])
        
        for i in range(nrow):
            for j in range(ncol):
                res += min(rows_max[i], cols_max[j]) - grid[i][j]
        return res