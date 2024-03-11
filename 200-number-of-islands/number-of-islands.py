class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0, 1], [1, 0], [-1,0], [0, -1]]
        nrow = len(grid)
        ncol = len(grid[0]) 
        visited = set()
        
        def get_nei(x,y):
            neigh = []
            for dx, dy in dirs:
                nx, ny = dx+x, dy+y
                if 0<=nx<nrow and 0 <= ny < ncol:
                    neigh.append((nx, ny)) 

            return neigh

        def bfs(x, y):
            queue = collections.deque() 
            queue.append((x, y))

            
            while queue:
                cur_x, cur_y = queue.popleft()
                for nx, ny in get_nei(cur_x, cur_y):
                    if (nx,ny) not in visited and grid[nx][ny] == "1":
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        res = 0
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    res += 1
        return res  





        