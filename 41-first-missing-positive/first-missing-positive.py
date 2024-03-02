class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        nums_set = set(nums)

        max_val = max(nums_set) 
        
        if 1 not in nums_set:
            return 1

        for i in range(1, max_val+2):
            print(i)
            if i not in nums_set:
                print('here')
                return i
