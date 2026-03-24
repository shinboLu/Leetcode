class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights) 
        res = float('inf') 

        def check(mid):
            cur_w = 0 
            cur_day = 1 

            for w in weights:
                if cur_w + w > mid:
                    cur_day +=1 
                    cur_w = w
                else:
                    cur_w += w
            return cur_day <= days

        while left <= right:
            mid = (left+right)//2
            if check(mid):
                res = min(res, mid)
                right = mid-1
            else:
                left =mid+1
        return res
