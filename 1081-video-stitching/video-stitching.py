class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        dp = [float('inf')] * (time + 1)

        dp[0] = 0

        for i in range(1, time + 1):
            for start, end in clips:
                if start <= i <= end:
                    dp[i] = min(dp[start] +1, dp[i])

        if dp[time] == float('inf'):
            return -1

        return dp[time]