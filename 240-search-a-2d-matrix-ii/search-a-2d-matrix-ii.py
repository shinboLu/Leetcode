class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow = len(matrix)
        ncol = len(matrix[0]) 

        for row in range(nrow):
            for col in range(ncol):
                if matrix[row][col] == target:
                    return True
        return False
