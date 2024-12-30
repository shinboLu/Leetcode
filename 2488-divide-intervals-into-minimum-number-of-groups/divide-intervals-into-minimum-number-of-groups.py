class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        point_to_count = collections.defaultdict(int)

        for i in intervals:
            point_to_count[i[0]] += 1
            point_to_count[i[1]+1] -= 1 

        concurrent_intervals = 0 
        max_concurrent_intervals = 0 

        for point in sorted(point_to_count.keys()):
             concurrent_intervals += point_to_count[point] 
             max_concurrent_intervals = max(max_concurrent_intervals, concurrent_intervals)
        return max_concurrent_intervals