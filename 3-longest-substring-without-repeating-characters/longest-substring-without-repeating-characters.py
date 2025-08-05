class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapping = {}
        left, right = 0, 0
        res =0 

        while right < len(s):
            right_char = s[right]
            right +=1
            mapping[right_char] = mapping.get(right_char, 0)+1

            while mapping[right_char] > 1:
                mapping[s[left]] = mapping.get(s[left])-1
                left+=1
            res = max(res, right-left)  

        return res