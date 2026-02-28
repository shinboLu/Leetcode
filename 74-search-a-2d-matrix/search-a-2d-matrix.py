class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow = len(matrix)
        ncol = len(matrix[0])
        
        left = 0 
        right = nrow*ncol -1 

        while left <= right:
            mid = (left+right)//2 
            if matrix[mid//ncol][mid%ncol] == target:
                return True
            
            if matrix[mid//ncol][mid%ncol] < target:
                left = mid + 1
            else:
                right = mid -1 

        return False