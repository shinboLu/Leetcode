class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        DIR = [[0,1], [1,0], [-1,0], [0,-1]]
        nrow = len(board)
        ncol = len(board[0])
        queue = collections.deque()
        if ncol == 0:
            return 

        for row in range(nrow):
            for col in range(ncol):
                if (row == 0 or col == 0 or row == nrow-1 or col == ncol -1) and board[row][col] == 'O':
                    queue.append((row, col))
        
        while queue:
            r, c = queue.popleft()
            board[r][c] = "Need Reverse Back"
            for dx, dy in DIR:
                new_x, new_y = r + dx, c + dy

                if 0 <= new_x < nrow and 0 <= new_y < ncol and board[new_x][new_y] == 'O':
                    queue.append((new_x, new_y))

        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Need Reverse Back':
                    board[i][j] = 'O'
