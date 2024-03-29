class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def bt(idx, combs):
            if len(combs) == k:
                res.append(combs.copy())
                return

            for i in range(idx, n+1):
                combs.append(i)
                bt(i+1, combs)
                combs.pop()
        bt(1, [])
        return res