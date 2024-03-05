class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        nrow = len(matrix)
        ncol = len(matrix[0])
        prev_row = [0] * ncol
        res = 0 

        for row in range(nrow):
            cur_row = matrix[row].copy()
            print(cur_row)
            for col in range(ncol):
                if cur_row[col] != 0:
                    cur_row[col] += prev_row[col] 

            sorted_row = sorted(cur_row, reverse=True)

            for i in range(ncol):
                res = max(res, sorted_row[i] * (i+1))

            prev_row = cur_row 

        return res 

