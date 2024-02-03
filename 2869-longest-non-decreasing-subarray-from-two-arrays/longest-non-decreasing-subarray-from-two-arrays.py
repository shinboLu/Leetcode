class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache
        def dp(idx, prev_val):
            if idx == len(nums1):
                return 0
            
            res = 0

            if not prev_val:
                 res = dp(idx+1, prev_val)

            if prev_val <= nums1[idx]:
                res = max(res, dp(idx+1, nums1[idx])+1)
            
            if prev_val <= nums2[idx]:
                res = max(res, dp(idx+1, nums2[idx])+1)

            return res 

        return dp(0,0)


        