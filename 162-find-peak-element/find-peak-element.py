class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right = len(nums)-1
        if len(nums) == 1:
            return 0
        
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        while left < right: 
            mid = (left+right)//2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid 
            
            elif nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1 

        return right
