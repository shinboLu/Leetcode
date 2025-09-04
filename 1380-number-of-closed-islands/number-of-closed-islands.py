class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        dirs = [[0,1], [1, 0], [-1, 0], [0, -1]]
        res = 0 
        nrow = len(grid)
        ncol = len(grid[0])
        visited = [[False] * ncol for _ in range(nrow)]

        def getNeis(x, y):
            neis = [] 
            for dx, dy in dirs:
                nx, ny = dx+x, dy+y
                if 0<=nx<nrow and 0<=ny<ncol:
                    neis.append((nx,ny))

            return neis

        def bfs(x, y):
            is_closed = True
            queue = collections.deque()
            queue.append((x, y))
            if x == 0 or x == nrow-1 or y == 0 or y == ncol-1:
                is_closed = False
            visited[x][y] = True
            while queue:
                cur_x, cur_y = queue.popleft()
                for neix, neiy in getNeis(cur_x, cur_y):
                    if grid[neix][neiy] == 0 and not visited[neix][neiy]:
                        if neix == 0 or neix == nrow-1 or neiy == 0 or neiy == ncol-1:
                            is_closed = False
                        visited[neix][neiy] = True
                        queue.append((neix, neiy))
            return is_closed
        
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == 0 and not visited[row][col]:
                    if bfs(row, col):
                        res+=1
        return res
