class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = cur_max = cur_min = nums[0]

        for i in range(1, len(nums)):
            cur_num = nums[i]
            temp_max = max(cur_num, cur_max * cur_num, cur_min * cur_num)
            cur_min = min(cur_num, cur_max * cur_num, cur_min * cur_num)
            cur_max = temp_max
            res = max(res, cur_max)

        return res 
