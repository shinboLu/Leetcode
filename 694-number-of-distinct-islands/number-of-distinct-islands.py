class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        visited = set() 
        


        def dfs(x, y, dir):
            nonlocal islands_path
            if x < 0 or x >= nrow or y < 0 or y >= ncol:
                return 
            if (x, y) in visited or grid[x][y] == 0:
                return
            visited.add((x, y))
            islands_path.append(dir)

            dfs(x+1, y, 'D')
            dfs(x, y+1, 'R')
            dfs(x-1, y, 'U')
            dfs(x, y - 1, 'L')
            ##The solution to this is that we also need to record where we backtracked. 
            ##      This occurs each time we exit a call to the dfs(...) function. 
            ##      We'll do this by appending a 0 to the string.
            islands_path.append('0')

        unique_islands = set()
        for row in range(nrow):
            for col in range(ncol):
                islands_path = []
                dfs(row, col, '')
                if islands_path:
                    unique_islands.add(tuple(islands_path))
        return len(unique_islands)



