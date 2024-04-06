class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = max_len = 0 

        indices = {}

        for i, num in enumerate(nums):
            prefix_sum += num 

            if prefix_sum == k:
                max_len = i + 1 

            if prefix_sum - k in indices:
                max_len = max(max_len, i - indices[prefix_sum - k])
            
            if prefix_sum not in indices:
                indices[prefix_sum] = i 

        return max_len