class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float('inf')

        res =0 

        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            res = max(res, prices[i] - min_p)

        return res 