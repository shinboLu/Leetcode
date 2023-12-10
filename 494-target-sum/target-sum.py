class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtracking(idx, total):
            if idx == len(nums):
                if total == target:
                    return 1
                else: 
                    return 0

            key = (idx, total)
            if key in memo:
                return memo[key]

            memo[key] = (backtracking(idx+1, total+nums[idx]) + backtracking(idx+1, total - nums[idx]))

            return memo[key]

        return backtracking(0,0)