class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or num_rows >= len(s):
            return s
        res = [''] * num_rows
        cur_idx = 0 
        cur_dir = 1

        for char in s:
            res[cur_idx] += char

            if cur_idx == 0:
                cur_dir = 1
            elif cur_idx >= num_rows-1:
                cur_dir = -1

            cur_idx += cur_dir
        return ''.join(res)