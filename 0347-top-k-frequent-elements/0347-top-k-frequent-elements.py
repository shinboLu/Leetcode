from heapq import heappop, heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        heapq = []
        res = []
        for key, val in counter.items():
            heappush(heapq, [-val, key])
        
        for i in range(k):
            val, key = heappop(heapq)
            res.append(key)
        return res



            


        