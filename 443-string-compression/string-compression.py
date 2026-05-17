class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0 
        res = 0 
        while i < len(chars): 
            group_len = 1
            while i+group_len < len(chars) and chars[i+group_len] == chars[i]:
                group_len +=1
            chars[res] = chars[i] 
            res +=1

            if group_len > 1: 
                str_repr = str(group_len)
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr) 
            i+=group_len
        return res