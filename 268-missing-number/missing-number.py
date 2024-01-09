from heapq import heapify, heappop, heappush 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        res = 0

        if nums[0] != 0:
            res = nums[0]-1
        elif nums[-1] != len(nums):
            res = nums[-1] + 1

        else:
            for i in range(1,len(nums)):
                if nums[i] - nums[i-1] > 1:
                    res = nums[i] -1

        return res 
