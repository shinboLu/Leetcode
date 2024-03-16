import bisect
class Solution:
    def minimizeSet(self, d1: int, d2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        lcm = math.lcm(d1, d2)
        def check(x: int) -> bool:
            left1 = max(uniqueCnt1 - x // d2 + x // lcm, 0)
            left2 = max(uniqueCnt2 - x // d1 + x // lcm, 0)
            common = x - x // d1 - x // d2 + x // lcm
            return common >= left1 + left2
        return bisect.bisect_left(range((uniqueCnt1 + uniqueCnt2) * 2 - 1), True, key=check)
