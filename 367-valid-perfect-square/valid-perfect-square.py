class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 or num==4:
            return True 
        left = 0
        right = num//2-1 

        while left <= right:
            mid = (left+right)//2

            if mid ** 2 == num:
                return True
            elif mid**2 < num:
                left = mid+ 1
            else:
                right = mid-1

        return False