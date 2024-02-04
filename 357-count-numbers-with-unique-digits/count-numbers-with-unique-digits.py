class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1 
        if n == 1: return 10

        res = 10

        prefix = 9

        for i in range(2, n+1):
            prefix *= (11-i)
            res += prefix
        
        return res