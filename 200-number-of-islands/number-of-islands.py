class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0,1], [1,0], [-1,0],[0,-1]]
        nrow = len(grid)
        ncol = len(grid[0])
        visited = set()

        def dfs(x, y):
            visited.add((x,y))
            for dx, dy in dirs:
                nx, ny = dx+x, dy+y
                if 0<=nx<nrow and 0<=ny<ncol and grid[nx][ny] == "1" and (nx,ny) not in visited:
                    dfs(nx, ny) 
        res = 0
        for row in range(nrow):
            for col in range(ncol):
                if (row, col) not in visited and grid[row][col] == '1':
                    dfs(row, col)
                    res+=1
        return res