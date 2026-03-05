class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_tracker = []
        for idx, intv in enumerate(intervals):
            start_tracker.append((intv[0], idx))

        start_tracker.sort(key = lambda x: x[0])

        def binary_search(start_tracker, target):
            left = 0 
            right = len(start_tracker)-1
            res = -1
            while left <=right:
                mid = (left+right)//2
                if start_tracker[mid][0] >= target:
                    res = start_tracker[mid][1]
                    right = mid-1
                else:
                    left = mid+1
            return res
        res = []
        for s, e in intervals:
            idx = binary_search(start_tracker, e)
            res.append(idx)

        return res