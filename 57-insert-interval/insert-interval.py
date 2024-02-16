class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x :x[0])

        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start > res[-1][1]:
                res.append([start, end])

            elif end > res[-1][1]:
                res[-1][1] = end

        return res 

