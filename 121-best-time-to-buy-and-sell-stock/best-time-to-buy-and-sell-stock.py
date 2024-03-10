class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = float('inf')
        res = 0

        for i in range(n):
            min_price = min(min_price, prices[i]) 
            if prices[i] - min_price > res:
                res = prices[i] - min_price
        return res 
            