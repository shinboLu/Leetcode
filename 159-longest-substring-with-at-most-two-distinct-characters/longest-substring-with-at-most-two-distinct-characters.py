class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 3: 
            return len(s)
        
        res = 0 
        left, right = 0, 0
        count = {} 

        while right < len(s):
            #print(count)
            count[s[right]] = right 
            right += 1

            if len(count) == 3:
                left_most = min(count.values())
                del count[s[left_most]]
                left = left_most + 1

            res = max(res, right - left) 

        return res 
