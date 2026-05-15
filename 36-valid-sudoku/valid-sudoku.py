class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_counter = collections.defaultdict(list)
        col_counter = collections.defaultdict(list)
        matrix_counter = collections.defaultdict(lambda: collections.defaultdict(list))
        nrow = len(board)
        ncol = len(board[0])

        for row in range(nrow):
            for col in range(ncol):
                if board[row][col] != '.':
                    if board[row][col] in row_counter[row]:
                        return False
                    elif board[row][col] in col_counter[col]:
                        return False
                    elif board[row][col] in matrix_counter[row//3%3][col//3%3]:
                        return False
                row_counter[row].append(board[row][col])
                col_counter[col].append(board[row][col])
                matrix_counter[row//3%3][col//3%3].append(board[row][col])
        return True

