class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        dirs = [[0,1], [1,0], [-1,0], [0, -1]]
        INF = 2147483647 
        nrow = len(rooms)
        ncol = len(rooms[0])
        visited = set()
        queue = collections.deque()
        for row in range(nrow):
            for col in range(ncol):
                if rooms[row][col] == 0:
                    queue.append((row, col)) 

        def bfs(queue):
            while queue:
                cx, cy = queue.popleft()
                for dx, dy in dirs:
                    nx, ny = cx+dx, cy+dy
                    if 0<=nx<nrow and 0<=ny<ncol and (nx, ny) not in visited:
                        if rooms[nx][ny] == INF:
                            rooms[nx][ny] = rooms[cx][cy]+1
                            visited.add((nx, ny))
                            queue.append((nx, ny))
        bfs(queue)
