class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or num_rows >= len(s): 
            return s
        cur_dir = 1
        row = [""] * num_rows
        print(row)
        cur_idx = 0

        for char in s:
            row[cur_idx] += char

            if cur_idx ==0:
                cur_dir = 1
            elif cur_idx == num_rows-1:
                cur_dir = -1
            
            cur_idx += cur_dir
        return ''.join(row)
            

 
            
