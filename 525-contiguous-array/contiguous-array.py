class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = float('-inf') 
        prefix_sum = [0] * (len(nums)+1)

        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + (-1 if nums[i]==0 else 1)

        val_to_index = {}
        res = 0 
        for i in range(len(prefix_sum)):
            if prefix_sum[i] not in val_to_index:
                val_to_index[prefix_sum[i]] = i
            else:
                res = max(res, i - val_to_index[prefix_sum[i]])

        return res
