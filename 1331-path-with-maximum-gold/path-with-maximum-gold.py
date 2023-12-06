class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        DIR = [[0,1], [1,0], [-1,0], [0, -1]]
        nrow, ncol = len(grid), len(grid[0])
        visited = set()
        max_gold = 0

        def backtracking(x, y, cur):
            nonlocal max_gold
            if x < 0 or x > nrow-1 or y < 0 or y > ncol-1 or grid[x][y]==0 or (x,y) in visited:
                return
            
            max_gold = max(max_gold, cur+grid[x][y])

            visited.add((x,y))
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                backtracking(nx, ny, cur+grid[x][y])

            visited.remove((x,y))

        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] != 0:
                    backtracking(row, col, 0)

        return max_gold