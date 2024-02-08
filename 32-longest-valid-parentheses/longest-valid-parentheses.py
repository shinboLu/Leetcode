class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0 
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_length = max(left*2, max_length)

            elif right > left:
                left, right = 0, 0

        left, right = 0,0

        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_length = max(left * 2, max_length)
            elif left > right:
                left, right = 0, 0 

        return max_length
