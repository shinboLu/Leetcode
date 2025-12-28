class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        island_a = collections.deque()
        visited = set()
        distance = 0
        def dfs_get_landA(x, y):
            island_a.append((x,y))
            visited.add((x, y))
            for dx, dy in dirs:
                nx, ny = dx+x, dy+y
                if 0<=nx<n and 0<=ny<n and (nx, ny) not in visited and grid[nx][ny]==1:
                    dfs_get_landA(nx, ny)
        start_x, start_y = 0, 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    start_x, start_y = row, col
                    break
        dfs_get_landA(start_x, start_y)
        

        def bfs(queue):
            nonlocal distance
            while queue:
                for _ in range(len(queue)):
                    cx, cy = queue.popleft()
                    for dx, dy in dirs:
                        nx, ny = dx+cx, dy+cy
                        if 0<=nx<n and 0<=ny<n and (nx, ny) not in visited:
                            if grid[nx][ny] == 1: 
                                return distance
                            else:
                                visited.add((nx, ny))
                                queue.append((nx, ny))
                distance +=1

        return bfs(island_a)

