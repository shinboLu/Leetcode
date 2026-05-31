class Solution:
    def compress(self, chars: List[str]) -> int:
        cur_idx = 0 
        write_idx = 0 

        while cur_idx < len(chars):
            cur_count = 0 

            while cur_idx+cur_count < len(chars) and chars[cur_idx] == chars[cur_idx+cur_count]:
                cur_count +=1 

            chars[write_idx] = chars[cur_idx]
            write_idx +=1
            if cur_count > 1:
                str_cur_count = str(cur_count)
                chars[write_idx:write_idx+len(str_cur_count)] = list(str_cur_count)
                write_idx += len(str_cur_count)
            cur_idx+=cur_count
        return write_idx