class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        

        for start, end in intervals[1:]:
            if start > res[-1][1]:
                res.append([start, end])
            elif end > res[-1][-1]:
                res[-1][1] = end

        return res