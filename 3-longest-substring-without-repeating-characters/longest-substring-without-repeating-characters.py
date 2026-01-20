class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapping = collections.defaultdict(int)
        left = 0 
        right = 0
        maxi = 0 

        
        while right < len(s):
            cur = s[left:right+1]
            set_cur = set(cur)
            if len(cur) == len(set_cur):
                right += 1
                maxi  = max(maxi, right-left)
            else:
                while right < len(s) and left <=right and len(cur) > len(set_cur):
                    left += 1
                    cur = s[left:right+1]
                    set_cur = set(cur)
        return maxi
            
