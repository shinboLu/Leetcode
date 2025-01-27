class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ''
        for c in s:
            if c.isalnum():
                ns+=c.lower()
        left = 0
        right = len(ns)-1

        while left < right:
            if ns[left] == ns[right]:
                left += 1
                right -=1 
            else:
                return False

        return True
