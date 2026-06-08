class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counter = {0:-1}
        res = 0
        prefix_sum = 0

        for idx, val in enumerate(nums):
            if val == 0:
                prefix_sum -=1
            else:
                prefix_sum +=1
            if prefix_sum in counter:
                res = max(res, idx-counter[prefix_sum])
            else:
                counter[prefix_sum] = idx

        return res