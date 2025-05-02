class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        i = 0
        while i < len(s):
            sub_string = {}
            sub_string[s[i]] = i 
            j = i + 1
            while j < len(s) and s[j] not in sub_string.keys():
                sub_string[s[j]] = j
                j = j + 1 
            res = max(res, len(sub_string))
            if j >= len(s):
                return res 

            i = sub_string[s[j]] + 1
 
        return res 
