class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        DIR = [[0,1], [1,0], [-1,0], [0, -1]]
        

        def getNeighbors(x, y):
            neighbor = []
            for dx, dy in DIR:
                new_x, new_y = dx + x, dy + y
                if 0 <= new_x < nrow and 0 <= new_y < ncol:
                    neighbor.append([new_x, new_y])
            return neighbor

        
        def bfs(x, y):
            queue = collections.deque()
            queue.append([x, y])
            visited.add((x, y))
            area = 1

            while queue: 
                r, c = queue.popleft()
                for nx, ny in getNeighbors(r,c):
                    if grid[nx][ny] == 1 and (nx, ny) not in visited:
                        queue.append([nx, ny])
                        visited.add((nx, ny))
                        area += 1
            return area
        visited = set() 
        max_area = 0
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == 1 and (row,col) not in visited:
                    max_area = max(max_area, bfs(row, col))
        return max_area

                

                        