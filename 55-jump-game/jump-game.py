class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(idx):
            if idx == len(nums)-1:
                return True
            
            if idx >= len(nums) or nums[idx] == 0:
                return False
            
            for i in range(1, nums[idx]+1):
                if dfs(idx+i):
                    return True
            return False
        
        return dfs(0)
            