class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        res = 0 

        for num in unique_nums:
            if num-1 not in unique_nums:
                cur_len = 1
                cur_num = num
                while cur_num+1 in unique_nums:
                    cur_len+=1
                    cur_num+=1
                res = max(res, cur_len)
        return res