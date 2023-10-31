class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])

        DIR = [[0,1], [0,-1], [1, 0], [-1,0]]

        def getNeighbors(x, y):
            neighbor = []
            for dx, dy in DIR:
                new_x, new_y = dx + x, dy + y
                if 0 <= new_x < nrow and 0 <= new_y < ncol:
                    neighbor.append([new_x, new_y])
            return neighbor

        def bfs(x, y):
            queue = collections.deque()
            queue.append([x,y])
            curr_area = 1
            while len(queue) > 0:
                n = len(queue)
                level = []
                for _ in range(n):
                    start_x, start_y = queue.popleft()
                    for neighbor in getNeighbors(start_x, start_y):
                        nx, ny = neighbor
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 'v'
                            curr_area += 1
                            queue.append([nx, ny])
            return curr_area
        
        max_area = 0

        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] ==1:
                    grid[r][c] = 'v'
                    max_area = max(max_area, bfs(r,c))
        return max_area




        