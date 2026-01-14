class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def check(row, col):
            ## check row

            row1 = grid[row][col] + grid[row][col+1] + grid[row][col+2]
            row2 = grid[row+1][col] + grid[row+1][col+1] + grid[row+1][col+2]
            row3 = grid[row+2][col] + grid[row+2][col+1] + grid[row+2][col+2]

            if not (row1 == row2 == row3):
                return False

            col1 = grid[row][col] + grid[row+1][col] + grid[row+2][col]
            col2 = grid[row][col+1] + grid[row+1][col+1] + grid[row+2][col+1]
            col3 = grid[row][col+2] + grid[row+1][col+2] + grid[row+2][col+2]

            if not (col1 == col2 == col3 == row1):
                return False
            visited = set()
            for i in range(3):
                for j in range(3):
                    if grid[row+i][col+j] > 9 or grid[row+i][col+j] < 1:
                        return False
                    if grid[row+i][col+j] in visited:
                        return False
                    visited.add(grid[row+i][col+j])
            diagonal1 = grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2] 
            diagonal2 = grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col] 

            if not (diagonal1 == diagonal2 == row1):
                return False
            return True
        
        nrow = len(grid)
        ncol = len(grid[0])
        res = 0
        for row in range(nrow-2):
            for col in range(ncol-2):
                if check(row, col):
                    res +=1

        return res




                


            
