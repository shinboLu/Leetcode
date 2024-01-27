class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n)
        dp[0] = 1
        cur_len = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                cur_len += 1
            else:
                cur_len = 1
            dp[i] = dp[i-1] + cur_len

        return dp[-1]


