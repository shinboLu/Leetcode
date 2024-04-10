from heapq import heapify, heappop
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        ops = 0
        left, right = 0, len(nums)-1

        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -=1 
                ops +=1
            
            elif nums[left] + nums[right] < k:
                left += 1

            else:
                right -=1

        return ops