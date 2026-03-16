class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        lcm = math.lcm(divisor1, divisor2) 

        left = 1
        right = 10 ** 31

        while left <= right:
            mid = (left+right) //2 
            if uniqueCnt1 <= mid - mid//divisor1 and uniqueCnt2 <= mid-mid//divisor2 and uniqueCnt1+uniqueCnt2 <= mid - mid // lcm:
                right = mid -1
            else:
                left = mid+1
        return left