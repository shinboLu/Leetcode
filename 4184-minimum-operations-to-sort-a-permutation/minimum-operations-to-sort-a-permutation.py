class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums) 
        idx_0 = nums.index(0)

        def check(step):
            for i in range(1, n):
                prev = (idx_0 + (i-1) * step) % n
                cur = (idx_0 + i * step) % n
                if nums[prev] > nums[cur]:
                    return False
            return True
        res = float('inf')
        if check(1):
            res = min(res, idx_0)
            res = min(res, n - idx_0 + 2)

        if check(-1):
            res = min(res, idx_0+2)
            res = min(res, n-idx_0)

        return -1 if res == float('inf') else res