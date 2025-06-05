class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(left, right):
            right -=1 
            while left <= right:
                if s[left] != s[right]:
                    return False
                left +=1
                right -=1 
            return True
        for length in range(len(s), 0, -1):
            for left in range(len(s)-length+1):
                right = left+length
                if palindrome(left, right):
                    return s[left:right]

        return ""
