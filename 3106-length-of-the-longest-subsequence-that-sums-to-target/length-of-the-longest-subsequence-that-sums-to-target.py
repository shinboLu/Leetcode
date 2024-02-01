class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        ## need to decide nums[i] can contribute to the current solutions

        dp = [float('-inf')] * (target+1)
        dp[0] = 0

        for num in nums: 
            for i in range(target, -1, -1):
                if i - num >= 0:
                    dp[i] = max(dp[i], dp[i-num]+1)
        print(dp)
        return dp[-1] if dp[-1]!=float('-inf') else -1 