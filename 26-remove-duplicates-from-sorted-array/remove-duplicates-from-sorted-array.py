class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0

        while right <= len(nums)-1:
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
        return left+1


