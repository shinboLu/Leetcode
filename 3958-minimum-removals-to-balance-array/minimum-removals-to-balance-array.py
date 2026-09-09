class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        res =0
        left = 0 
        
        for right in range(len(nums)):
            while left < right and nums[right] > nums[left] * k:
                left +=1
            
            res = max(res, right-left+1)
        
        return len(nums)-res
