from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        DIR = [[1,0], [0,1], [-1, 0], [0, -1]]
        nrow = len(grid)
        ncol = len(grid[0])

        visited = set() 
        queue = collections.deque()
        queue.append(((0,0, k, 0)))

        while queue:
            cur_x, cur_y, left, steps = queue.popleft() 
            if (cur_x, cur_y, left) in visited or left < 0:
                continue
            if (cur_x, cur_y) == (nrow -1, ncol-1):
                return steps 

            visited.add((cur_x, cur_y, left))

            if grid[cur_x][cur_y] == 1: 
                left -= 1

            for dx, dy in DIR:
                nx, ny = dx + cur_x, dy + cur_y
                if 0 <= nx < nrow and 0 <= ny < ncol:
                    queue.append((nx, ny, left, steps + 1))

        return -1


