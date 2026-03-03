class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow = len(matrix)
        ncol = len(matrix[0])

        ## dir = 0: search in row
        ## dir = 1: search in col

        def binary_search(start, direction):
            if direction == 0:
                left = 0
                right = ncol-1
            else:
                left = 0
                right = nrow-1
            while left <= right:
                mid = (left+right)//2

                if direction == 0:
                    val = matrix[start][mid]
                else:
                    val = matrix[mid][start]
                
                if val == target:
                    return True
                elif val < target:
                    left = mid + 1 
                else:
                    right = mid -1
            return False

        for i in range(min(nrow, ncol)):
            row_find = binary_search(i, 0)
            col_find = binary_search(i, 1)
            if row_find or col_find:
                return True
        return False

                
