class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        queue = collections.deque()

        nrow = len(matrix)
        ncol = len(matrix[0])

        for r in range(nrow):
            for c in range(ncol):
                if matrix[r][c] == 0:
                    queue.append([r, c])

        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(nrow):
                matrix[i][cur_y] = 0
            for j in range(ncol):
                matrix[cur_x][j] = 0