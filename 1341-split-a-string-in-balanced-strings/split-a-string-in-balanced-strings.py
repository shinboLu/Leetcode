class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left, right = 0, 0
        
        res = 0 

        for ch in s: 
            if ch == 'L':
                left += 1
            if ch == 'R':
                right += 1
            if left == right:
                res += 1 

        return res 