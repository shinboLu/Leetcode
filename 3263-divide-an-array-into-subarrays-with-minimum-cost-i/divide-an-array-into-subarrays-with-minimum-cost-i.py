class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cur_cost = nums[0]
        
        cur_cost += sum(sorted(nums[1:])[:2])
        return cur_cost
