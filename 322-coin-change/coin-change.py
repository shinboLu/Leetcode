class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## dp[i]: when target is i, need dp[i] amount of coins

        dp = [amount + 1] * (amount+1)

        dp[0] = 0
        #print(dp)

        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue

                dp[i] = min(dp[i], 1 + dp[i-coin])

        return -1 if dp[amount] == amount + 1 else dp[amount]