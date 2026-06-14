class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum_map = collections.defaultdict(int) 
        prefix_sum_map[0] = 1
        cur_sum = 0
        res = 0 
        for num in nums:
            cur_sum += num
            res += prefix_sum_map[cur_sum-goal]
            prefix_sum_map[cur_sum] +=1
        return res