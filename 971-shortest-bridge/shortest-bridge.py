class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        visited =set()
        queue = collections.deque()
        def dfs_find_island(x, y):
            visited.add((x, y))
            queue.append((x, y))
            for dx, dy in dirs:
                nx, ny = dx+x, dy+y
                if 0<=nx<n and 0 <= ny < n and grid[nx][ny] == 1 and (nx, ny) not in visited:
                    dfs_find_island(nx, ny)
        
        
        first_x = 0
        first_y = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    first_x = row
                    first_y = col
                    break
        dfs_find_island(first_x, first_y)

        distance = 0
        while queue:
            for _ in range(len(queue)):
            # new_bfs = collections.deque()
                cur_x, cur_y = queue.popleft()
                for dx, dy in dirs:
                    nx, ny = dx+cur_x, dy+cur_y
                    if 0<=nx<n and 0<=ny<n and (nx,ny) not in visited: 
                        if grid[nx][ny] == 1:
                            print(f"Found second island at ({nx}, {ny}), distance={distance}")
                            return distance
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        # elif grid[nx][ny] == 0:
                            # new_bfs.append((nx, ny))
                            # visited.add((nx, ny))
            distance += 1
            # queue = new_bfs
        return distance





