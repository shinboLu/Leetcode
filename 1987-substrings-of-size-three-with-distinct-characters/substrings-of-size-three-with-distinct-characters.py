class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = []
        for i in range(len(s)-2):
            cur_sub = s[i:i+3]
            if len(set(cur_sub)) == 3:
                res.append(cur_sub)

        return len(res) 

