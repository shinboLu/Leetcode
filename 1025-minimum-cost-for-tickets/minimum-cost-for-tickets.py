class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = float('inf')
                ## j: determine the next day we need to purchase a ticket
            j = i
            for d,c in zip([1,7,30], costs):
                ## check the next purchase date is in bound, and is smaller that the current day + the ticket validate days 
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
            return dp[i]

        return dfs(0)