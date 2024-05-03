class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        cur = set()
        max_len = float('-inf')

        for right in range(len(s)):
            while s[right] in cur:
                cur.remove(s[left])
                left += 1

            cur.add(s[right])
            max_len = max(max_len, right-left+1)

        return max_len

