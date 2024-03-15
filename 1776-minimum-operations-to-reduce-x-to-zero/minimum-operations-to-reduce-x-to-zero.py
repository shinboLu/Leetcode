class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        tot_sum = sum(nums) 
        
        left = 0
        res = float('inf')

        for right in range(len(nums)):
            tot_sum -= nums[right] 

            while tot_sum < x and left <= right:
                
                tot_sum += nums[left] 
                left += 1

            if tot_sum == x:
                res = min(res, (len(nums)-1-right) + left)

        return res if res != float('inf') else -1 

            