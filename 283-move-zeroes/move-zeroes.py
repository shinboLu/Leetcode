class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0 
        right = 0

        while right <= len(nums)-1:
            if nums[right] == 0:
                right += 1
            else:
                nums[left], nums[right] = nums[right], nums[left] 
                left += 1
                right += 1
            