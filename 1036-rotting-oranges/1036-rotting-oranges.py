class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIR = [(1,0), (-1,0), (0,1), (0,-1)]
        nrow, ncol = len(grid), len(grid[0])
        if nrow == 0:
            return -1

        fresh_apples = 0
        time = 0
        queue = collections.deque()
        
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 2:
                    queue.append((i, j))   
                elif grid[i][j] == 1:
                    fresh_apples += 1
                    
        while len(queue) > 0 and fresh_apples > 0:
            time += 1
            n = len(queue)
            for _ in range(n):
                row, col = queue.popleft()
                for dx, dy in DIR: 
                    new_x, new_y = dx + row, dy + col
                    if new_x < 0 or new_x == nrow or new_y < 0 or new_y == ncol:
                        continue
                    if grid[new_x][new_y] == 0 or grid[new_x][new_y] ==2:
                        continue
                    fresh_apples -= 1
                    grid[new_x][new_y] =2
                    queue.append((new_x, new_y))
        
        return time if fresh_apples == 0 else -1
                        

        