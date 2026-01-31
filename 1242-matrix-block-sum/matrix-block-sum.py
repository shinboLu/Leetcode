class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        nrow = len(mat)
        ncol = len(mat[0])

        prefix_sum = [[0 for _ in range(ncol+1)] for _ in range(nrow+1)]
        
        for i in range(1, nrow+1):
            for j in range(1, ncol+1):
                prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + mat[i-1][j-1]

        res = [[0 for _ in range(ncol)] for _ in range(nrow)]

        for i in range(nrow):
            for j in range(ncol):
                r1 = max(0, i-k)+1
                c1 = max(0, j-k)+1
                r2 = min(nrow-1, i+k) +1
                c2 = min(ncol-1, j+k)+1
                res[i][j] = prefix_sum[r2][c2] - prefix_sum[r2][c1-1] - prefix_sum[r1-1][c2] + prefix_sum[r1-1][c1-1]

        return res