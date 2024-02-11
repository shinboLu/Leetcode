class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        res = float('inf')
        
        def dfs(idx):
            nonlocal res
            if idx >= n-1:
                return 0
            
            if idx in memo:
                return memo[idx]

            for i in range(idx, idx + nums[idx]):
                res = min(res, dfs(i+1) + 1)

            memo[idx] = res
            return res
        return dfs(0)
            

