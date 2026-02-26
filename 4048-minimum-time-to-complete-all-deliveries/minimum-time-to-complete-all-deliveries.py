class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        left = 0 
        right = 10 ** 18 
        multi = lcm(r[0], r[1])

        while left < right:
            mid = (left+right)//2 

            if d[0] <= mid - mid // r[0] and d[1] <= mid - mid // r[1] and sum(d) <= mid - mid//multi:
                right = mid
            else:
                left = mid + 1

        return left