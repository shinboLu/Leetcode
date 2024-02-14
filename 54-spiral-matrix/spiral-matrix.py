class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nrow = len(matrix)
        ncol = len(matrix[0])
        visited = 101
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        cur_direction = 0
        change_direction = 0
        
        cur_row, cur_col = 0,0

        res = [matrix[0][0]]

        matrix[cur_row][cur_col] = visited

        while change_direction < 2:
            while True:
                next_row = cur_row + directions[cur_direction][0]
                next_col = cur_col + directions[cur_direction][1] 

                if not (0<=next_row < nrow and 0 <= next_col <ncol):
                    break
                if matrix[next_row][next_col] == visited:
                    break

                change_direction = 0
                cur_row, cur_col = next_row, next_col 
                res.append(matrix[cur_row][cur_col])
                matrix[cur_row][cur_col] = visited

            cur_direction = (cur_direction + 1) % 4
            change_direction +=1
        return res 
