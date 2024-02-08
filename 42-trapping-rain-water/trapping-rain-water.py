class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_dp = [0] * n
        right_dp = [0] * n
        res = 0 
        left_dp[0] = height[0]
        right_dp[n-1] = height[n-1]

        for i in range(1, n):
            left_dp[i] = max(height[i], left_dp[i-1])

        for i in range(n-2, -1, -1):
            right_dp[i] = max(height[i], right_dp[i+1])

        for i in range(1, n-1):
            res += min(left_dp[i], right_dp[i]) - height[i]
        
        return res 

        

