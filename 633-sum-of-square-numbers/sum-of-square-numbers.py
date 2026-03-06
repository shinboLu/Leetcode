class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0 
        while a**2 <= c:
            b = (c-a**2) ** 0.5
            print(b)
            if b == int(b):
                return True
            a +=1 
        return False