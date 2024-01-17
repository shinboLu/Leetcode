class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 1
        numIncr = 1
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                numIncr += 1
            else:
                numIncr = 1
            dp[i] = dp[i - 1] + numIncr
        return dp[n - 1]