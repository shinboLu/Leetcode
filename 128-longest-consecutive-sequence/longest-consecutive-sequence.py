class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            nxt = num-1 
            cur = 0 

            if nxt not in nums_set:
                while nxt + 1 in nums_set:
                    cur += 1
                    nxt+=1
            
            res = max(res, cur)

        return res 