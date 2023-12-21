class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        backtracked = [0] * len(candidates)
        res = []

        def backtracking(start_index, combs):
            if sum(combs) == target:
                res.append(combs.copy())
                return
            
            if sum(combs) > target:
                return 

            
            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                
                combs.append(candidates[i])
                backtracking(i+1, combs)
                combs.pop()

        backtracking(0,[])
        return res 
