
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_counter = collections.defaultdict(list)
        col_counter = collections.defaultdict(list)
        grid_counter = collections.defaultdict(lambda : collections.defaultdict(list))

        for i in range(9):
            for j in range(9):
                cur_val = board[i][j]

                if cur_val != '.':
                    if cur_val in row_counter[i] or cur_val in col_counter[j] or cur_val in grid_counter[i//3%3][j//3%3]:
                        return False

                    row_counter[i].append(cur_val)
                    col_counter[j].append(cur_val)
                    grid_counter[i//3%3][j//3%3].append(cur_val)
        return True