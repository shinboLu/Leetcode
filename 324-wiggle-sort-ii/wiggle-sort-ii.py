class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = sorted(nums)
        n = len(nums)
        left, right = 1, n-1

        for _ in range(2):
            for i in range(left, n, 2):
                nums[i] = temp[right]
                right -= 1
            left -= 1
        