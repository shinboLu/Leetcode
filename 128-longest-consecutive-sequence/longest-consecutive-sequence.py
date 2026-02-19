class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        unique = set(nums)

        for num in unique:
            if num-1 not in unique:
                cur_streak = 1
                cur_num = num

                while cur_num +1 in unique:
                    cur_num+=1
                    cur_streak +=1
                
                res = max(res, cur_streak)

        return res