class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            odds = {}
            evens = {}
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    odds[nums[j]] = odds.get(nums[j], 0) +1
                else: 
                    evens[nums[j]] = evens.get(nums[j], 0) + 1
                
                if len(odds) == len(evens):
                    max_len = max(max_len, j - i+1) 
        return max_len
            
