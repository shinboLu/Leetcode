class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)
        def bt(combs):
            if len(combs) == len(nums):
                res.append(combs.copy())

            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                visited[i] = True
                combs.append(nums[i])
                bt(combs)
                visited[i] = False
                combs.pop()

        bt([])
        return res