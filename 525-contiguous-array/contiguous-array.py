class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mapping = {0:-1}
        prefix_sum = 0
        res = 0 

        for idx, val in enumerate(nums):
            if val == 0:
                prefix_sum += -1
            else:
                prefix_sum += 1 
            
            if prefix_sum in mapping:
                prev_idx = mapping[prefix_sum]
                length = idx - prev_idx
                res = max(res, length)
            else:
                mapping[prefix_sum] = idx
        return res