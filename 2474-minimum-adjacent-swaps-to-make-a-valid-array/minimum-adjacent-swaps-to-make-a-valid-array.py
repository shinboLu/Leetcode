class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min_val = min(nums)
        min_idx = nums.index(min_val)
        new_nums = [nums[min_idx]] + nums[:min_idx] + nums[min_idx+1:]

        max_val = max(nums)
        max_idx = new_nums[::-1].index(max_val) 

        return min_idx + max_idx



