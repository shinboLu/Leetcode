class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(subgrid, row, col):
            visited = [False] * 10

            for i in range(3):
                for j in range(3):
                    num = subgrid[i+row][j+col]
                    if num<1 or num>9:
                        return False
                    if visited[num]:
                        return False
                    visited[num] = True
            
            row1 = subgrid[row][col] + subgrid[row][col+1] + subgrid[row][col+2]
            row2 = subgrid[row+1][col] + subgrid[row+1][col+1] + subgrid[row+1][col+2]
            row3= subgrid[row+2][col] + subgrid[row+2][col+1] + subgrid[row+2][col+2]

            if row1 != row2 != row3:
                return False
            
            col1 = subgrid[row][col] + subgrid[row+1][col] + subgrid[row+2][col]
            col2 = subgrid[row][col+1] + subgrid[row+1][col+1] + subgrid[row+2][col+1]
            col3 = subgrid[row][col+2] + subgrid[row+1][col+2] + subgrid[row+2][col+2]

            if col1 != col2 != col3:
                return False

            d1 = subgrid[row][col] + subgrid[row+1][col+1] + subgrid[row+2][col+2]
            d2 = subgrid[row][col+2] + subgrid[row+1][col+1] + subgrid[row+2][col]
            if d1!=d2:
                return False
            return True
        nrow = len(grid)
        ncol = len(grid[0])
        res = 0
        for i in range(nrow-2):
            for j in range(ncol-2):
                if check(grid, i, j ):
                    res+=1

        return res

                
                
            
