class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = float('inf')
        while left <= right:
            cur_speed = (left+right)//2
            cur_time = 0 
            for pile in piles:
                cur_time += math.ceil(pile/cur_speed)
            if cur_time <= h:
                right = cur_speed -1 
                res = min(res, cur_speed)
            else:
                left = cur_speed+1

        return res