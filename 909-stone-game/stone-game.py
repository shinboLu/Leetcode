class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        dp = [0] * (n+1)
        dp[1] = max(piles[0], piles[-1])
        dp[2] = max(piles[1], piles[-2])
        for i in range(3, n+1):
            dp[i] = max(dp[i-1], dp[i-2])+piles[i-1] 

        print(dp) 

        return dp[-1] > dp[-2]
        