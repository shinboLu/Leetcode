class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        nrow = len(board)
        ncol = len(board[0]) 


        def dfs(x, y):
            if x < 0 or x >= nrow or y < 0 or y >= ncol or board[x][y] != 'O':
                return 
            board[x][y] = 'T'
            for dx, dy in dirs:
                dfs(dx+x, dy+y)
        
        for x in range(nrow):
            for y in [0, ncol-1]:
                dfs(x, y)
        for x in range(ncol):
            for y in [0, nrow-1]:
                dfs(y, x)

        for x in range(nrow):
            for y in range(ncol):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'T':
                    board[x][y] = 'O'