class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        n = len(nums) 
        dp = [0] * (n+1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            rob = dp[i-2] + nums[i]
            no_rob = dp[i-1] 
            dp[i] = max(rob, no_rob)

        return max(dp)