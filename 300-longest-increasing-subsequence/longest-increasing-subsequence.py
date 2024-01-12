class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ## dp: at index i, dp[1] is the length of the maximum increase length for nums[i]
        dp = [1] * n

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        print(dp)
        return max(dp) 
            



                