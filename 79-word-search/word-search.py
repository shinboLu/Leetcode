class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrow = len(board)
        ncol = len(board[0])
        dirs = [[0,1], [1,0], [-1, 0], [0, -1]]
        combs = [board[0][0]]

        def backtrack(row, col, remain_letter):
            if len(remain_letter) == 0:
                return True
            
            if not(0<=row<nrow) or not(0<=col<ncol) or board[row][col] != remain_letter[0]:
                return False

            res = False
            temp = board[row][col]
            board[row][col] = '#' 

            for dx, dy in dirs:
                res = backtrack(dx+row, dy+col, remain_letter[1:])
                if res:
                    break  

            board[row][col] = temp 

            return res

        for i in range(nrow):
            for j in range(ncol):
                if backtrack(i, j, word):
                    return True
        return False 