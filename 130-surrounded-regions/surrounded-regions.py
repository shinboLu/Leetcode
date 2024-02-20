class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [[1, 0], [0,1], [-1, 0], [0, -1]]
        nrow = len(board)
        ncol = len(board[0])
        visited = set() 
        queue = collections.deque()

        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == 'O' and (i == 0 or j== 0 or i == nrow-1 or j == ncol-1):
                    queue.append((i, j))

        def getNeigh(x ,y):
            nei = [] 
            for dx, dy in dirs: 
                nx, ny = dx + x, dy + y
                if 0 <= nx < nrow and 0 <= ny < ncol:
                    nei.append((nx, ny))

            return nei 

        while queue:
            cur_x, cur_y = queue.popleft()
            board[cur_x][cur_y] = 'R'
            for nx, ny in getNeigh(cur_x, cur_y):
                if board[nx][ny] == 'O':
                    queue.append((nx, ny))
        
        
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == 'R':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
         




                

        