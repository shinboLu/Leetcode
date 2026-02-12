class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nrow = len(matrix)
        ncol = len(matrix[0])
        res = []
        left = 0 
        right = ncol-1

        up = 0 
        down = nrow-1

        while len(res) < nrow * ncol:
            for col in range(left, right+1):
                res.append(matrix[left][col])

            for row in range(up+1, down+1):
                res.append(matrix[row][right])

            
            if up != down:
                for col in range(right-1, left-1, -1):
                    res.append(matrix[down][col])

            if left != right:
                for row in range(down-1, up, -1):
                    res.append(matrix[row][left]) 

            left +=1 
            right-=1
            up+=1
            down-=1

        return res
