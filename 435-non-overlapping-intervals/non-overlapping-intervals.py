class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        prev_s, prev_e = intervals[0] 
        res = 0
        print(intervals)
        for itv in intervals[1:]:
            cur_s, cur_e = itv
            if cur_s < prev_e:
                res +=1
            else:
                prev_s = cur_s
                prev_e = cur_e
        return res
