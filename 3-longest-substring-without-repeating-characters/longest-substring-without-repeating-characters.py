class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        res = 0 
        cur_s = set()
        for right in range(len(s)):
            while s[right] in cur_s:
                cur_s.remove(s[left])
                left +=1 
            cur_s.add(s[right])
            res = max(res, right-left+1)

        return res
