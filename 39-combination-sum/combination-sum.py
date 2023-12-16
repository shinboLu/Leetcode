class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(index, combs):
            if sum(combs) == target:
                res.append(combs.copy())
                return

            if sum(combs) > target:
                return 
            
            for i in range(index, len(candidates)):
                combs.append(candidates[i])
                bt(i, combs)
                combs.pop()
            
        bt(0, [])
        return res 
