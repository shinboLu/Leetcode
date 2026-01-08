class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        dirs = [[0,1], [1,0], [-1,0], [0, -1]]
        INF = 2147483647
        nrow = len(rooms) 
        ncol = len(rooms[0])
        def dfs(x, y, distance):
            if x < 0 or x >= nrow or y < 0 or y >= ncol or rooms[x][y] == -1:
                return 

            if distance > 0 and rooms[x][y] <= distance:
                return 
            rooms[x][y] = distance

            for dx, dy in dirs:
                nx, ny = dx+x, dy+y
                dfs(nx, ny, distance+1)

        for row in range(nrow):
            for col in range(ncol):
                if rooms[row][col] == 0:
                    dfs(row, col, 0)
            