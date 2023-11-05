class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIR = [[1,0], [0,1], [-1, 0], [0,-1]]
        nrow = len(grid)
        ncol = len(grid[0])
        visited = set()

        def getNeighbors(x,y):
            neighbor = []
            for dx, dy in DIR:
                new_x, new_y = dx + x, dy + y
                if 0 <= new_x < nrow and 0 <= new_y < ncol:
                    neighbor.append([new_x, new_y])
            return neighbor

        def bfs(x, y):
            queue = collections.deque()
            queue.append((x,y))
            visited.add((x,y))
            islands = []
            
            while len(queue) > 0:
                n = len(queue)
                for _ in range(n):
                    r,c = queue.popleft()
                    for neighbor_x, neighbor_y in getNeighbors(r,c):
                        if (neighbor_x, neighbor_y) not in visited and grid[neighbor_x][neighbor_y] == '1':
                            visited.add((neighbor_x, neighbor_y))
                            queue.append((neighbor_x, neighbor_y))

        islands = 0
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == '1' and (row,col) not in visited:
                    islands += 1
                    bfs(row, col)
                    
        return islands

            
