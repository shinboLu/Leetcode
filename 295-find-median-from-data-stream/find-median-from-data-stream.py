from heapq import heappush
class MedianFinder:

    def __init__(self):
        self.stream = []
        self.length = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.stream, num)
        #print(self.stream)
        self.length += 1

    def findMedian(self) -> float:
        ## median flag, if == 1, return the actual median, else return the mean of the two middle values
        median = self.length // 2
        #print(median)
        ## edge case
        if self.length <= 1:
            return self.stream[0]
        elif self.length == 2:
            return (self.stream[0] + self.stream[1])/2
        else:
            if median == 1:
                return self.stream[median]
            else:
                left, right = 0, self.length-1

                while left < right:
                    left += 1
                    right -=1
            # print(left, right)
            # print(self.stream[left], self.stream[right])
            return (self.stream[left] + self.stream[right])/2
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()