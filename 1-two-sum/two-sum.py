from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = [] 
        tracker = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in tracker:
                return [i, tracker[remain]]
            else:
                tracker[nums[i]] = i 

        return 
