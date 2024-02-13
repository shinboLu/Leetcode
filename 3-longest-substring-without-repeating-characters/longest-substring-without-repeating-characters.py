class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        res = 0 
        count = collections.Counter()

        while right < len(s):
            r = s[right]
            count[r] += 1

            while count[r] > 1:
                l = s[left]
                count[l] -=1 
                left += 1

            res = max(res, right-left+1)

            right += 1

        return res