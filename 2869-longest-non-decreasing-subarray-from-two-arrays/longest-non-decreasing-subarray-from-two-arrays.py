class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i, prev):
            if i == len(nums1):
                return 0
            res = 0

            if not prev:
                res = dfs(i+1, prev)

            if prev <= nums1[i]:
                res = max(res, dfs(i+1, nums1[i])+1)
            if prev <= nums2[i]:
                res = max(res, dfs(i+1, nums2[i])+1)

            return res 

        return dfs(0,0)

            
            

