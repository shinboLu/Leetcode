class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        n = len(nums)
        visited = [False] * n

        def dfs(idx, combs):
            if len(combs) == n:
                res.append(combs.copy())
                return 
            
            if len(combs) > n:
                return 
            
            for i in range(n):
                if not visited[i]:
                    combs.append(nums[i])
                    visited[i]=True
                    dfs(i, combs) 
                    combs.pop()
                    visited[i]= False

        dfs(0, [])
        return res