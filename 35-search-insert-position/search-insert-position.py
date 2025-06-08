class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) -1 

        while left <= right: 
            mid = (left + right) // 2 
            print("mid val", nums[mid])

            if nums[mid] >= target:
                right = mid - 1 
            else: 
                left = mid + 1 
        return right +1
        
