class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        islands = 0
        DIR = [[1,0], [0,1], [0,-1], [-1, 0]]
        def bfs(x, y):
            queue = collections.deque([[x,y]])
            grid[x][y] = '0'
            while queue: 
                x,y = queue.popleft()
                for dirX, dirY in DIR:
                    dx, dy = dirX + x, dirY + y
                    if not is_valid(dx, dy):
                        continue
                    grid[dx][dy] = '0'
                    queue.append([dx, dy])

        def is_valid(x, y):
            return 0 <= x < nrow and 0 <= y < ncol and grid[x][y] == '1'

        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == '1':
                    ##start bfs()
                    bfs(i,j)
                    islands+=1
        return islands 
        
