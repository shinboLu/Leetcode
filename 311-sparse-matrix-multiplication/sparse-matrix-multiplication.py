class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        
        for row_idx, row in enumerate(mat1):
            for row_i, row_val in enumerate(row):
                if row_val:
                    for col_idx, col_val in enumerate(mat2[row_i]):
                        ans[row_idx][col_idx] += row_val * col_val

        return ans