class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum_count = {0:1}
        res = 0 
        cur_sum = 0 

        for num in nums:
            cur_sum += num
            res += prefix_sum_count.get(cur_sum%k, 0)
            prefix_sum_count[cur_sum%k] = prefix_sum_count.get(cur_sum%k, 0) + 1 
        return res