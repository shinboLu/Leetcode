class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums) 
        level = 1 
        
        while level < n:
            new_nums = []
            for i in range(1, len(nums)):
                new_nums.append((nums[i] + nums[i-1])%10)
            nums = new_nums
            level+=1
        return nums[0]

