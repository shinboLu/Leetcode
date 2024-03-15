class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums) 
        n = len(nums) 
        left = 0 
        prefix_sum = 0 
        max_len = -1

        for right in range(n):
            prefix_sum += nums[right] 
            while prefix_sum > total - x and left <= right:
                prefix_sum -= nums[left] 
                left += 1 
            
            if prefix_sum == total -x:
                max_len = max(max_len, right - left + 1)

        return n-max_len if max_len != -1 else -1 

            


