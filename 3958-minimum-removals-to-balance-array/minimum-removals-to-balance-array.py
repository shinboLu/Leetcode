class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0 
        right = 0
        res = -1

        for right in range(len(nums)):
            while left < len(nums) and nums[right] > nums[left]*k:
                left +=1
            res = max(res, right-left+1)

        return len(nums)- res if res != -1 else 0
