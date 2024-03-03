class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  
        left = 0 
        cur_sum = 0
        res = 0 

        for right in range(len(nums)):
            target = nums[right]
            cur_sum += target 

            while (right-left+1) * target - cur_sum > k:
                cur_sum -= nums[left]
                left += 1       

            res = max(res, right-left+1)

        return res 
            