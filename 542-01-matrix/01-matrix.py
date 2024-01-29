class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dists = [[0,1],[1,0], [-1, 0], [0, -1]]
        nrow = len(mat)
        ncol = len(mat[0])
        res = [row[:] for row in mat]
        def get_nei(x, y):
            nei = []
            for dx, dy in dists:
                nx, ny = x + dx, y + dy 
                if 0 <= nx < nrow and 0 <= ny < ncol:
                    nei.append((nx, ny)) 
            return nei
        queue = collections.deque()
        visited = set()
        for i in range(nrow):
            for j in range(ncol):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
                    visited.add((i,j))

        while queue:
            row, col, step = queue.popleft()
            for nx, ny in get_nei(row, col):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, step +1))
                    res[nx][ny] = step + 1

        return res

