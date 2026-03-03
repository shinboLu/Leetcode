class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        cur = 0
        res = float('inf')
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= target:
                res = min(res, right-left+1)
                cur -= nums[left]
                left +=1
        return res if res != float('inf') else 0