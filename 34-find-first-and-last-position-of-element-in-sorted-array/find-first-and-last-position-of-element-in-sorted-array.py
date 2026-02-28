class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def get_left(left, right):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid -1
            return left

        def get_right(left, right):
            while left <= right:
                mid = (left+right)//2  
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid -1
            return right

        left = get_left(0, len(nums)-1)
        right = get_right(0, len(nums)-1)

        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        return [left, right]