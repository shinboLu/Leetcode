class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(cur_idx, cur_comb):
            if sum(cur_comb) == target:
                res.append(cur_comb.copy())
                return
            if sum(cur_comb) > target:
                return 
            for i in range(cur_idx, len(candidates)):
                cur_comb.append(candidates[i]) 
                dfs(i, cur_comb)
                cur_comb.pop()
        cur_comb = []
        dfs(0, cur_comb)
        return res


