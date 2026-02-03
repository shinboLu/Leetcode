class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mapping = {0:-1}
        cur_sum = 0
        res=0

        for idx, val in enumerate(nums):
            if val == 0:
                cur_sum -=1
            else:
                cur_sum +=1
            
            if cur_sum in mapping:
                cur_idx = mapping[cur_sum]
                length = idx-cur_idx
                res = max(res, length)
            else:
                mapping[cur_sum] = idx
        return res