from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in dic:
                return [i, dic[remain]]
            else:
                dic[nums[i]] = i
        return -1


