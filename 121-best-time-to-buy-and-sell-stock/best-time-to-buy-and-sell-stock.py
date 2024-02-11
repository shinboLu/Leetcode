class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        res = 0

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            if min_price != float('inf') and prices[i] - min_price > res:
                res = prices[i] - min_price

        return res 