class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}

        for i in range(len(nums)):
            if nums[i] in sum_dict:
                return [sum_dict[nums[i]], i]
            else:
                sum_dict[target - nums[i]] = i
