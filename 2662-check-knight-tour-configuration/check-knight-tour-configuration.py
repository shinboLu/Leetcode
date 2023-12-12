class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        nrow = len(grid)
        ncol = len(grid[0])


        direction = [[2, 1], [1, 2],[-1, 2],[-2, 1], [-2, -1], [-1, -2], [1, -2],[2, -1]]
        
        def backtracking(x = 0, y = 0, count = 0 ):
            if count == nrow * ncol -1:
                return True
            
            for dx, dy in direction:
                nx, ny = dx + x, dy + y
                if nx < 0 or nx >= nrow or ny < 0 or ny >= nrow or grid[nx][ny] != grid[x][y] + 1:
                    continue

                if backtracking(nx, ny, count + 1):
                    return True

            return False

        return backtracking()


                    




            


