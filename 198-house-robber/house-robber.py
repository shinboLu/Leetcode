class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        #dp[i] stores the current max sum at index i from the decisions: rob or do not rob
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            take = nums[i] + dp[i-2]
            no_take = dp[i-1]
            dp[i] = max(take, no_take)
        return max(dp)  