from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = defaultdict(int)

        for idx, val in enumerate(nums):
            remains = target-val

            if remains in mapping.keys():
                return [idx, mapping[remains]]
            
            mapping[val] = idx

        