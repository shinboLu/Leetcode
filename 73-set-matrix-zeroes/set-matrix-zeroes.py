class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        nrow = len(matrix)
        ncol = len(matrix[0])

        directions = [[0,1], [-1,0], [0,1], [0,-1]]

        queue = collections.deque()

        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 0:
                    queue.append((i, j))

        
        while queue:
            cur_row, cur_col = queue.popleft()

            for i in range(nrow):
                for j in range(ncol):
                    if i == cur_row or j == cur_col:
                        matrix[i][j] = 0