class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def get_left_idx(left, right):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] >= target:
                    right = mid -1
                else:
                    left = mid + 1
            return left

        def get_right_idx(left, right):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] <= target:
                    left = mid + 1 
                else:
                    right = mid -1
            return right
        
        left_side = get_left_idx(0, len(nums)-1)
        if left_side == len(nums) or nums[left_side] != target:
            return [-1, -1]
        right_side = get_right_idx(0, len(nums)-1)
        
        return [left_side, right_side]