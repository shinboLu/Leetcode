class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0 
        right = 0 
        res = float('-inf')
        while right < len(s):
            cur_str = s[left:right+1]
            if len(set(cur_str)) == len(cur_str):
                res = max(len(cur_str), res)
                right += 1
            else:
                left+=1
        return res
            