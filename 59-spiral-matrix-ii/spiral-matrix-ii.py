class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right, top, bottom = 0, n-1, 0, n-1
        cur_num = 1
        matrix = [[0] * n for _ in range(n)] 

        while cur_num <= n**2:
            for i in range(left, right+1):
                matrix[top][i] = cur_num 
                cur_num += 1
            top += 1 

            for i in range(top, bottom+1):
                matrix[i][right] = cur_num 
                cur_num += 1

            right-=1 

            for i in range(right, left-1, -1):
                matrix[bottom][i] = cur_num 
                cur_num += 1 
            
            bottom -= 1

            for i in range(bottom, top-1, -1):
                matrix[i][left] = cur_num 
                cur_num += 1 
            left += 1

        return matrix

        