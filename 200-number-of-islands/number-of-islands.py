class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0,1], [1,0], [-1,0],[0,-1]]
        nrow = len(grid)
        ncol = len(grid[0]) 
        
        def bfs(x, y):
            queue = collections.deque()
            queue.append([x, y])
            grid[x][y] = '0'
            while queue: 
                curx, cury = queue.popleft()
                
                for dx, dy in dirs:
                    nx, ny = curx+dx, cury+dy
                    if 0<=nx<nrow and 0<= ny < ncol and grid[nx][ny]=='1':
                        grid[nx][ny] = '0'
                        queue.append([nx, ny])
        res = 0 
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == '1':
                    bfs(row, col)
                    res +=1
        return res
