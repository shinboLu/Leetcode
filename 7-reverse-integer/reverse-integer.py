class Solution:
    def reverse(self, x: int) -> int:
        neg = False if x >= 0 else True

        x = str(abs(x))
        x = x[::-1]
        if neg:
            res = -int(''.join(x)) 
        else:
            res= int(''.join(x)) 
        
        return res if res in range(-2**31, 2**31-1) else 0

