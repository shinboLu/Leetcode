class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 1
        right = max(quantities)

        def get_x(mid):
            cur_sum = 0 
            for q in quantities:
                cur_sum += math.ceil(q/mid)
            return cur_sum

        while left < right:
            mid = (left+right)//2
            res = get_x(mid)
            if res <= n: 
                right = mid
            else:
                left = mid+1
        return left


