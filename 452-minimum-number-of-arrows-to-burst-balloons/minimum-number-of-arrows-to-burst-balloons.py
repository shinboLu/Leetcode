class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # sort by x_end
        points.sort(key = lambda x : x[1])

        res = [points[0]]
        print(points)
        for start, end in points[1:]:
            if start > res[-1][1]:
                res.append([start, end])
            elif end < res[-1][1]:
                res[-1][1] = end
        print(res)
        return len(res)
