class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = collections.deque()
        nrow = len(board)
        ncol = len(board[0])

        if ncol == 0:
            return 
        DIR = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(nrow):
            for j in range(ncol):
                if (i ==0 or j ==0 or i == nrow - 1 or j == ncol - 1) and board[i][j] == 'O':
                    queue.append([i,j])
        
        while queue:
            x, y = queue.popleft()
            board[x][y] = 'T'
            for dirX, dirY in DIR:
                dx, dy = x + dirX, y + dirY

                if 0 <= dx < nrow and 0 <= dy < ncol and board[dx][dy] == 'O':
                    queue.append([dx, dy])
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
