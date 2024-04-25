class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = total = longest = 0 

        for right in range(len(s)):
            total += abs(ord(s[right]) - ord(t[right]))

            while total > maxCost:
                total -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            longest = max(longest, right-left+1)

        return longest