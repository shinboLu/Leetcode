class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right = len(nums)-1

        while left + 1 < right:
            mid = (left+right)//2 
            if nums[mid] <= nums[mid+1]:
                left = mid
            
            else:
                right = mid
        
        if nums[left] < nums[right]:
            return right
        return left
