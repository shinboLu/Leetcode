class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow = len(matrix)
        ncol = len(matrix[0])

        start_row = nrow-1
        start_col = 0 


        while start_row >= 0 and start_col < ncol:
            if matrix[start_row][start_col] > target:
                start_row -= 1
            elif matrix[start_row][start_col] < target:
                start_col += 1
            else:
                return True


        return False
