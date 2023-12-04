class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow, ncol = len(matrix), len(matrix[0])

        i = nrow-1
        j = 0

        while i >= 0 and j < ncol:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False