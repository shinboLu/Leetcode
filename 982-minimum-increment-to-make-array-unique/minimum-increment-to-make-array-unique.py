class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        n = len(nums)

        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                diff = nums[i-1] + 1 - nums[i]
                res += diff
                nums[i] = nums[i-1] + 1

        return res



