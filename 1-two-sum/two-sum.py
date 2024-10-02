from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = [] 
        mapping = {}
        for i in range(len(nums)):
            remains = target - nums[i]
            if remains in mapping:
                res = [i, mapping[remains]]

            else:
                mapping[nums[i]] = i

        return res