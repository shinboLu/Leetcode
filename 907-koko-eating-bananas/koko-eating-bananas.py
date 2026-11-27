class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_speed = 1 
        max_speed = max(piles)

        while min_speed <= max_speed:
            test_speed = (min_speed+max_speed)//2 
            cur_h = 0 
            for p in piles:
                cur_h += math.ceil(p/test_speed)
            if cur_h > h:
                min_speed = test_speed +1
            else:
                max_speed = test_speed-1
        return min_speed