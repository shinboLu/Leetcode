class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        gmax = arrays[0][-1]
        gmin = arrays[0][0]
        res = 0

        for arr in arrays[1:]:
            start = arr[0]
            end = arr[-1]

            res = max(end-gmin, gmax - start, res)

            gmin = min(gmin, start)
            gmax = max(gmax, end)

        return res