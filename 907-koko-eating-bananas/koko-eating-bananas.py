class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left+right)//2 
            cur_hours = 0 
            for pile in piles:
                cur_hours += math.ceil(pile/mid) 
            if cur_hours <= h:
                right = mid-1
            else:
                left = mid+1

        return left

        