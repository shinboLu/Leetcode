class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        print(intervals)
        res = 1
        cur_end = intervals[0][1]

        for i in range(len(intervals)):
            if intervals[i][0] >= cur_end:
                res+=1
                cur_end = intervals[i][1]

        return len(intervals) - res