class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        res = 0 

        for num in unique:
            if num-1 not in unique:
                search_start = num
                cur_len = 1

                while search_start+1 in unique:
                    cur_len += 1
                    search_start+=1
                res = max(res, cur_len)
        return res