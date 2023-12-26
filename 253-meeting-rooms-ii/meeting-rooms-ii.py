from heapq import heapify, heappop, heappush
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        hq = []

        heappush(hq, intervals[0][1])

        for i in intervals[1:]:
            if hq[0] <= i[0]:
                heappop(hq)

            heappush(hq, i[1])

        return len(hq)
            



        