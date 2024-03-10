class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        left, right = 0, len(nums)-1
        if nums[right] > nums[0]:
            return nums[0]

        while left <= right:
            middle = (left+right)//2

            if nums[middle] > nums[middle+1]:
                return nums[middle+1]
            
            if nums[middle-1] > nums[middle]:
                return nums[middle]
            
            if nums[middle] > nums[left]:
                left = middle + 1

            else:
                right = middle -1

