class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res = 1
        n = len(nums)

        #last wiggle direction
        last_wiggle = None

        for i in range(1, n):
            cur_diff = nums[i] - nums[i-1]
            if (cur_diff > 0 and last_wiggle != 1) or (cur_diff < 0 and last_wiggle != -1 ):
                res += 1
                last_wiggle = 1 if cur_diff > 0 else -1

        return res


