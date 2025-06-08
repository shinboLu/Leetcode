class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        left = self.findLeft(nums, target)
        right = self.findRight(nums, target)

        return [left, right]
    def findLeft(self, nums, target):
        left, right= 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        print(right+1)
        return right+1 if right+1 >= 0 and right+1 <= len(nums)-1 and nums[right+1] == target else -1

    def findRight(self, nums, target):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid -1 

        return right if right >= 0 and nums[right] == target else -1

