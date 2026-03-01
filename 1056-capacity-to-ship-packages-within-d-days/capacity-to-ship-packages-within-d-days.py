class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = float('inf')

        def check(mid):
            cur_cap = mid
            cur_days = 1
            for w in weights:
                if cur_cap - w < 0:
                    cur_days +=1
                    cur_cap = mid
                cur_cap -= w
            return cur_days <= days

        while left <= right:
            mid = (left+right)//2
            if check(mid):
                res = min(res, mid)
                right = mid -1
            else:
                left = mid + 1 

        return res