class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrow = len(board)
        ncol = len(board[0])
        dirs = [[0,1], [1,0], [0,-1], [-1, 0]]


        queue = collections.deque()
        for row in range(nrow):
            for col in range(ncol):
                if (row ==0 or col ==0 or row == nrow-1 or col == ncol-1) and board[row][col]=='O':
                    queue.append([row, col])

        while queue:
            cx, cy = queue.popleft()
            board[cx][cy] = 'V'
            for dx, dy in dirs:
                nx, ny = dx+cx, dy+cy
                if 0<=nx<nrow and 0<=ny<ncol and board[nx][ny] == 'O':
                    queue.append([nx, ny]) 
        for row in range(nrow):
            for col in range(ncol):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'V':
                    board[row][col]='O'

        

        
