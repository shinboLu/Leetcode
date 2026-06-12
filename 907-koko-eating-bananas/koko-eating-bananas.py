class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) 
        tot = sum(piles)

        while left < right:
            cur_speed = (left+right)//2
            tot_time = 0 

            for pile in piles:
                tot_time+= math.ceil(pile/cur_speed)
            if tot_time <= h:
                right = cur_speed
            else:
                left = cur_speed+1
        return left
