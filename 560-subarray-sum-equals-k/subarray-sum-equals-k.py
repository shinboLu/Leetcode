class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_mapper = {0:1}
        prefix_sum = 0 
        res = 0 
        for num in nums:
            prefix_sum += num
            if prefix_sum -k in prefix_sum_mapper:
                res+= prefix_sum_mapper[prefix_sum-k]
            if prefix_sum not in prefix_sum_mapper:
                prefix_sum_mapper[prefix_sum] =1
            else:
                prefix_sum_mapper[prefix_sum] += 1
        return res
            
