class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        should_increase = True
        for i in range(len(nums)-1):
            if should_increase != (nums[i]<=nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
            should_increase = not should_increase