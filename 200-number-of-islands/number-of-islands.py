class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return 
            if grid[x][y] != '1':
                return 
            grid[x][y] = '0'

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x, y+1)
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=='1':
                    res+=1
                    dfs(row, col)
        return res



