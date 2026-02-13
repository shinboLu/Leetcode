class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0,1], [1,0], [-1,0],[0,-1]]
        nrow = len(grid)
        ncol = len(grid[0])
        visited = set()

        def dfs(x, y):
            if x < 0 or x >= nrow or y < 0 or y >= ncol or (x, y) in visited or grid[x][y] == '0':
                return 
            visited.add((x, y))
            for dx, dy in dirs:
                nx, ny = dx+x, dy +y 
                dfs(nx, ny) 
        res = 0
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == '1' and (row, col) not in visited:
                    dfs(row, col) 
                    res +=1 
        return res

