class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []

        left = 0

        while left < len(nums):
            cur = nums[left]
            while left + 1 < len(nums) and nums[left] + 1 == nums[left+1]:
                left += 1
            if cur != nums[left]:
                res.append(str(cur) + '->' + str(nums[left]))
            
            else:
                res.append(str(nums[left]))

            left += 1
        return res