class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        nrow = len(board)
        ncol = len(board[0])

        def dfs(x, y):
            if x<0 or x >= nrow or y < 0 or y >=ncol or board[x][y]!='O':
                return
            board[x][y] = 'V'

            for dx, dy in dirs:
                nx, ny = dx+x, dy+y
                dfs(nx, ny)

        for row in range(nrow):
            for col in [0, ncol-1]:
                dfs(row, col)

        for col in range(ncol):
            for row in [0, nrow-1]:
                dfs(row, col)
        print(board)

        for row in range(nrow):
            for col in range(ncol):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] =='V':
                    board[row][col] = 'O'




