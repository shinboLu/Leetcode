class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        for start, end in intervals:
            if not res:
                res.append([start, end])
            if start <= res[-1][1]:
                temp = res.pop()
                start = min(temp[0], start) 
                end = max(temp[1], end)
                res.append([start, end])
            else:
                res.append([start, end])
        return res