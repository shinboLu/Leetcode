class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nrow = len(matrix)
        ncol = len(matrix[0]) 
        row_s = 0 
        row_e = nrow-1
        col_s = 0
        col_e = ncol-1

        res = []

        while len(res) < nrow * ncol:
            for col in range(col_s, col_e+1): 
                res.append(matrix[row_s][col])
            
            for row in range(row_s+1, row_e+1):
                res.append(matrix[row][col_e])
            
            if row_s != row_e:
                for col in range(col_e-1, col_s-1, -1):
                    res.append(matrix[row_e][col])

            if col_s != col_e:
                for row in range(row_e-1, row_s, -1):
                    res.append(matrix[row][col_s])
            row_s+=1
            row_e-=1
            col_s+=1
            col_e-=1 
        return res