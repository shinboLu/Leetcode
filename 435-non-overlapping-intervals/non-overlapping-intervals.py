class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1]) 
        res = 1
        prev_s, prev_e = intervals[0]
        print(intervals)
        for i in range(1, len(intervals)):
            cur_s, cur_e = intervals[i]
            if cur_s >= prev_e:
                res+=1
                prev_s = cur_s
                prev_e = cur_e

        return len(intervals)-res