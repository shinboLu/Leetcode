class Solution:
    def trailingZeroes(self, n: int) -> int:
        

        def factorial(num):
            if num == 0:
                return 1
            
            return num * factorial(num-1)
        
        num = factorial(n)
        
        res = 0 

        while num % 10 == 0:
            res += 1
            num //= 10

            
        return res