class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        left = 1 
        right = 1 * 10**20
        multiplier = math.lcm(divisor1, divisor2) 
        while left < right:
            mid = (left+right)//2 
            if uniqueCnt1 <= mid - mid // divisor1 and uniqueCnt2 <= mid - mid // divisor2 \
            and uniqueCnt1 + uniqueCnt2 <= mid - mid // multiplier:
                right = mid 
            else:
                left = mid + 1

        return left
