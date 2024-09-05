class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0 
        window = {}
        res = 0 

        while right < len(s): 
            cur_l = s[right]
            right += 1
            window[cur_l] = window.get(cur_l, 0) + 1

            while window.get(cur_l) > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            
            res = max(res, right-left)
        return res 