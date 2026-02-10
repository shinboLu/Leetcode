class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        start = nums[0]

        _next = sorted(nums[1:])

        return start + sum(_next[:2])