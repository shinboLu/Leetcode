class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        visited = [False] * len(nums)

        def backtrack(combs):
            if len(combs) == len(nums):
                res.append(combs.copy())
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                combs.append(nums[i])
                backtrack(combs)
                combs.pop()
                visited[i] = False

        backtrack([])
        return res