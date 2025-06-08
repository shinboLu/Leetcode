class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        orders = {val[0]: idx for idx, val in enumerate(intervals)}
        sorted_start = sorted(orders.keys())
        starts = []
        res = []
        for i in range(len(intervals)):
            starts.append(self.binarySearch(sorted_start, intervals[i][1]))

        for start_val in starts: 
            if start_val is not None:
                res.append(orders[start_val])
            else:
                res.append(-1)
        return res

    def binarySearch(self,sorted_start, target):
        left = 0
        right = len(sorted_start)-1
        while left <= right:
            mid = (left+right)//2 

            if sorted_start[mid] < target:
                left = mid + 1 
            else:
                right = mid -1 

        if right+1 < 0 or right + 1 >= len(sorted_start):
            return None
        else:
            return sorted_start[right+1]