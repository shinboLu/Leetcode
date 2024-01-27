class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        def dfs(idx): 
            if idx == len(days):
                return 0
            if idx in dp:
                return dp[idx]

            dp[idx] = float('inf')
            for d, c in zip([1,7,30], costs):
                j = idx
                while j < len(days) and days[j] < days[idx] + d:
                    j+=1

                dp[idx] = min(dp[idx], c + dfs(j))
            return dp[idx]
        return dfs(0)


        return 0