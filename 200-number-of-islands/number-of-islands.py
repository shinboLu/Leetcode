class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0 
        dirs = [[0,1], [1, 0], [-1, 0], [0, -1]]
        nrow = len(grid)
        ncol = len(grid[0])
        visited = [[False] * ncol for _ in range(nrow)]

        def getNeis(x, y):
            neis = [] 
            for dx, dy in dirs:
                nx, ny = dx+x, dy + y 
                if 0 <= nx < nrow and 0 <= ny < ncol:
                    neis.append((nx, ny))
            return neis
        
        def bfs(x, y):
            queue = collections.deque()
            queue.append((x, y))
            while queue:
                cur_pos_x, cur_pos_y = queue.popleft()
                for nei_x, nei_y in getNeis(cur_pos_x, cur_pos_y):
                    if grid[nei_x][nei_y] == '1' and not visited[nei_x][nei_y]:
                        queue.append((nei_x, nei_y))
                        visited[nei_x][nei_y] = True
        
        for row in range(nrow):
            for col in range(ncol):
                if 0<=row<nrow and 0 <= col < ncol and grid[row][col] == '1' and not visited[row][col]:
                    bfs(row, col)
                    res+=1
        return res