class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [] 
        def backtracking(index, combs):
            if len(combs) == k:
                res.append(combs.copy())
                return

            for i in range(index, n + 1):
                combs.append(i)
                backtracking(i+1, combs)
                combs.pop()
        backtracking(1, [])
        return res