class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) 
        for i in range(n+1):
            left = bisect.bisect_left(nums, i)
            if left == n or nums[left] != i:
                return i
