class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1 
        if n == 1: return 10

        res = 10
        temp = 9

        for i in range(2, n+1):
            temp *= (11-i)
            res += temp

        return res 