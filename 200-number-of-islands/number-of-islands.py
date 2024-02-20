class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[1,0], [0,1], [-1,0], [0, -1]]
        visited = set()  
        res = 0
        nrow = len(grid)
        ncol = len(grid[0])

        def getNeighbors(x, y):
            neighbors = []
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy  
                if 0 <= nx < nrow and 0 <= ny < ncol:
                    neighbors.append((nx, ny))
            return neighbors 

        
        def bfs(x, y):
            queue = collections.deque()
            queue.append((x, y))

            while queue:
                x, y = queue.popleft()
                for nx, ny in getNeighbors(x, y):
                    if (nx, ny) not in visited and grid[nx][ny] != '0':
                        queue.append((nx, ny))
                        visited.add((nx, ny))
        
        for x in range(nrow):
            for y in range(ncol):
                if grid[x][y] == '1' and (x, y) not in visited:
                    res += 1
                    bfs(x, y)

        return res 




        