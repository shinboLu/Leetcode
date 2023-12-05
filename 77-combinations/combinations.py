class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtracking_update_res(combs, start, remain):
            if remain == 0:
                res.append(combs.copy())

            else:
                for i in range(start, n + 1 ):
                    combs.append(i)
                    backtracking_update_res(combs, i + 1, remain-1)
                    combs.pop()

        backtracking_update_res([], 1, k)
        return res
