class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtracking(idx, total):
            if idx == len(nums):
                return 1 if total == target else 0

            ## if the key exists, then it's in the cache, return it
            key = (idx, total)
            if key in dp:
                return dp[key]

            dp[key] = (backtracking(idx + 1, total + nums[idx]) +
                        backtracking(idx + 1, total - nums[idx]))
            
            return dp[(key)]

        return backtracking(0, 0)
        

            






            
