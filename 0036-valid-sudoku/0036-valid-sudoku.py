class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(n):
            for col in range(n):
                val = board[row][col]
                if val == '.':
                    continue
                if val in rows[row] or val in cols[col] or (val in boxes[row//3][col//3]):
                    return False
                
                rows[row].add(val)
                cols[col].add(val)
                boxes[row//3][col//3].add(val)
        return True

                





