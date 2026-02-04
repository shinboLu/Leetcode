class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        res = 0
        right = 0 


        while right < len(s): 
            cur = s[left:right+1]
            cur_set = set(cur) 

            while right < len(s) and left <= right and len(cur_set) != len(cur):
                left+=1
                cur = s[left:right+1]
                cur_set = set(cur) 
            
            right +=1
            res = max(right-left, res)

        return res