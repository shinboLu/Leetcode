class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur_sum = 0 
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            
            cur_sum += num
            res = max(cur_sum, res)
        return res