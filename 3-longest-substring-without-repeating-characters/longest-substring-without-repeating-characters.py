class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0 
        subset = set() 

        for right in range(len(s)):
            while s[right] in subset:
                subset.remove(s[left])
                left += 1
            subset.add(s[right])
            max_len = max(max_len, right-left+1)

        return max_len

                