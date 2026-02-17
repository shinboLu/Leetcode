class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        queue = collections.deque()
        dirs = [[0,1],[1,0], [-1,0], [0,-1]]
        tot = 0
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == 2:
                    queue.append([row, col])
                elif grid[row][col] == 1: 
                    tot +=1
        if tot == 0:
            return 0
        visited = set()
        count = 0 

        while queue:
            count+=1
            for i in range(len(queue)):
                cur_x, cur_y = queue.popleft()
                visited.add((cur_x, cur_y))
                print(visited)
                for dx, dy in dirs:
                    nx, ny = cur_x + dx, cur_y + dy
                    if 0<=nx<nrow and 0<=ny<ncol:
                        if (nx, ny) not in visited and grid[nx][ny] == 1: 
                            queue.append([nx, ny])
                            grid[nx][ny] = 2 
                            tot-=1

        return -1 if tot > 0 else count-1

