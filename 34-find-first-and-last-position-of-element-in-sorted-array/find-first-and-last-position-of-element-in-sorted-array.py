class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1

        left = self.getLeft(nums, target)
        right = self.getRight(nums, target)
        return [left, right]
    def getLeft(self, nums, target):
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2 
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid -1
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def getRight(self,nums, target):
        left = 0
        right = len(nums)-1
        while left <= right: 
            mid = (left+right)//2 
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = mid + 1
            if nums[mid] > target:
                right = mid -1

        if right < 0 or nums[right] != target:
            return -1
        return right


