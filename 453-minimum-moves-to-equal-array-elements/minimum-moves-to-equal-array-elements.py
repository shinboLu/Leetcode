class Solution:
    def minMoves(self, nums: List[int]) -> int:

        res = 0 
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            res += sorted_nums[i] - sorted_nums[0]
        return res 
