from heapq import heappush, heappop, heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        hq = [(-count, val) for val, count in counter.items()]
        heapify(hq)
        print(hq)

        res = [] 

        for i in range(k):
            count, val = heappop(hq)
            res.append(val)
        return res