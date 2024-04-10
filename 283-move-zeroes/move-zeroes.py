class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return 

        pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pointer] = nums[i]
                pointer += 1
        for i in range(pointer, len(nums)):
            nums[i] = 0

        