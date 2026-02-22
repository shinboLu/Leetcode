class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nrow = len(matrix) 
        ncol = len(matrix[0])
        res = []

        dirs = [[0,1], [1, 0], [0, -1], [-1, 0]] 

        steps = nrow * ncol
        start_r = 0 
        start_c = 0 
        end_c = ncol-1
        end_r = nrow-1

        while len(res) < nrow*ncol:
            for col in range(start_c, end_c+1):
                res.append(matrix[start_r][col])
            
            for row in range(start_r+1, end_r+1):
                res.append(matrix[row][end_c])
            
            if start_r!= end_r:
                for col in range(end_c-1, start_c-1, -1):
                    res.append(matrix[end_r][col])
            if start_c != end_c:
                for row in range(end_r-1, start_r, -1):
                    res.append(matrix[row][start_c])
            start_r+=1
            end_r-=1
            start_c+=1
            end_c-=1
        return res

            


