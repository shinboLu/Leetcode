class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        res = [] 

        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
                continue
            res_start, res_end = res.pop()
            intv_start, intv_end = intervals[i]
            if intv_start > res_end:
                res.append((res_start, res_end))
                res.append(intervals[i])
            else:
                res.append((min(res_start, intv_start), max(res_end, intv_end)))
        return res