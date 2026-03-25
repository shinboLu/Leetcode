class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        res = float('inf')
        cur_sum = 0 
        for right in range(len(nums)):
            cur_sum += nums[right]
        
            while cur_sum >= target:
                cur_len = right-left+1
                res = min(res, cur_len)
                cur_sum-= nums[left]
                left +=1
            
        return res if res != float('inf') else 0
