class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        def get_first(left, right): 
            while left <= right:
                mid = (left+right) //2
                if nums[mid] < target:
                    left = mid +1 
                else:
                    right = mid -1
            return left
        def get_last(left, right):
            while left <= right: 
                mid = (left+right)//2
                if nums[mid] > target:
                    right = mid -1 
                else:
                    left = mid +1 
            return right
        
        first = get_first(0, len(nums)-1)
        last = get_last(0, len(nums)-1)
        # print(first, last)
        if first > last or first == len(nums) or nums[first] != target:
            return [-1, -1]
        return [first, last]