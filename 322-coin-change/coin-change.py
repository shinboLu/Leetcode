class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(1, amount+1):
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)


        return dp[-1] if dp[-1] != amount+1 else -1 