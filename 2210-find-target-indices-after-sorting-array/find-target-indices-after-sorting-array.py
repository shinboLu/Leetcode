class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []

        for index, val in enumerate(nums):
            if val == target:
                res.append(index)

        return res 
