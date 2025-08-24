class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_counter = collections.defaultdict(list)
        col_counter = collections.defaultdict(list)
        matrix_counter = collections.defaultdict(lambda: collections.defaultdict(list))

        for row in range(9):
            for col in range(9):
                cur_val = board[row][col]

                if cur_val != '.':
                    if cur_val in row_counter[row] or cur_val in col_counter[col] or cur_val in matrix_counter[row//3%3][col//3%3]:
                        print(row_counter, col_counter, matrix_counter)
                        return False
                
                row_counter[row].append(cur_val)
                col_counter[col].append(cur_val)
                matrix_counter[row//3%3][col//3%3].append(cur_val)
        
        return True