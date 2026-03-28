class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow = len(matrix)
        ncol = len(matrix[0])

        def search_col(start, end, row):
            while start <= end:
                mid = (start+end)//2 

                if matrix[row][mid] == target:
                    return True
                
                if matrix[row][mid] < target:
                    start = mid +1
                else:
                    end = mid -1 
            return False
        def search_row(start, end, col):
            while start <= end:
                mid = (start+end)//2
                if matrix[mid][col] == target:
                    return True
                if matrix[mid][col] < target:
                    start = mid +1
                else:
                    end = mid -1 
            return False
        for i in range(min(nrow, ncol)):
            col_find = search_col(0, ncol-1, i)
            row_find = search_row(0, nrow-1, i)
            if col_find or row_find:
                return True
        return False

        