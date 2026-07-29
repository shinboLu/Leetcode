class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0 
        dirs = [[0,1], [1, 0], [-1, 0], [0, -1]] 
        nrow = len(grid)
        ncol = len(grid[0])
        tot_fresh = 0
        queue = collections.deque()
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == 1:
                    tot_fresh +=1
                if grid[r][c] == 2:
                    queue.append([r, c])
        if tot_fresh == 0:
            return 0
        if not queue and tot_fresh > 0:
            return -1
        
        while queue:
            
            cur_rot = 0
            for i in range(len(queue)):
                cx, cy = queue.popleft()
                for dx, dy in dirs:
                    nx, ny = dx+cx, dy+cy
                    if 0<=nx<nrow and 0<=ny<ncol and grid[nx][ny] ==1:
                        grid[nx][ny]=2
                        queue.append([nx, ny])
                        cur_rot +=1
            if cur_rot > 0:
                time +=1
            tot_fresh -= cur_rot 

        return time if tot_fresh == 0 else -1
